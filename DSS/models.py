from django.db import models

from parser_weather.parser import get_weather_data, prepare_weather_datetime, WEATHER_KEY


class Person(models.Model):
    lat = models.CharField(max_length=10, verbose_name='Широта (для определения погодных условий)')
    lon = models.CharField(max_length=10, verbose_name='Долгота (для определения погодных условий)')
    comfort_temperature_metric = models.PositiveSmallIntegerField(default=25, verbose_name='Комфортная температура')
    clothes = models.ManyToManyField('Clothes', verbose_name='Одежда, используемая, для формирования рекомендаций')

    def get_recommendation(self):
        temp, weather, wind_speed, wind_gust, dt = get_weather_data(self.lat, self.lon, WEATHER_KEY)
        dt = prepare_weather_datetime(dt)
        user_clothes = self.clothes.all()
        target = self.comfort_temperature_metric - temp
        recommendation_list = []
        for kind_of_clothes in ClosesKind.objects.all().order_by('-required'):
            clothes_in_kind = user_clothes.filter(kind=kind_of_clothes)
            recommended_cloth = None
            for cloth in clothes_in_kind:
                if abs(target - cloth.temp_resist) < abs(target - getattr(recommended_cloth, 'temp_resist', 0)):
                    recommended_cloth = cloth
            if recommended_cloth:
                recommendation_list.append(recommended_cloth)
        return ', '.join([getattr(item, 'name', '') for item in recommendation_list])


class ClosesKind(models.Model):
    name = models.CharField(max_length=100)
    required = models.BooleanField()
    allow_layers = models.BooleanField()

    def __str__(self):
        return self.name


class Clothes(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    allow_rain = models.BooleanField(verbose_name='допускается ношение в дождь')
    allow_snow = models.BooleanField(verbose_name='допускается ношение в снег')
    allow_wind = models.BooleanField(verbose_name='допускается ношение в ветер')
    temp_resist = models.IntegerField(verbose_name='Температурная устройчивость')
    kind = models.ForeignKey(ClosesKind, on_delete=models.CASCADE, related_name='clothes', verbose_name='Вид одежды')

    def __str__(self):
        return self.name
