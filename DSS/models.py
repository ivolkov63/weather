from django.db import models

from parser_weather.parser import get_weather_data, prepare_weather_datetime

key = ''


class Person(models.Model):
    lat = models.CharField(max_length=10)
    lon = models.CharField(max_length=10)
    comfort_temperature_metric = models.PositiveSmallIntegerField(default=25)
    clothes = models.ManyToManyField('Clothes')

    def get_weather(self):
        temp, weather, wind_speed, wind_gust, dt = get_weather_data(self.lat, self.lon, key)
        dt = prepare_weather_datetime(dt)

    def give_recommendation(self):
        user_clothes = str(self.user_clothes).split()

        if int(wind_gust) > 10 or int(wind_speed) > 10:
            weather_clothes_set = {}  # заполнить значениями {temp: clothes}
            need_clothes = [elem for elem in weather_clothes_set[temp] if elem not in user_clothes]
            unwanted_clothes = [elem for elem in user_clothes if elem not in weather_clothes_set[temp]]
        elif weather == 'rain':
            rainy_clothes_set = {}  # заполнить значениями {temp: clothes}
            need_clothes = [elem for elem in rainy_clothes_set[temp] if elem not in user_clothes]
            unwanted_clothes = [elem for elem in user_clothes if elem not in rainy_clothes_set[temp]]

        else:
            sunny_clothes_set = {}  # заполнить значениями {temp: clothes}
            need_clothes = [elem for elem in sunny_clothes_set[temp] if elem not in user_clothes]
            unwanted_clothes = [elem for elem in user_clothes if elem not in sunny_clothes_set[temp]]

        return f' temperature at {dt} is {temp}. Of the things you have, you will need {" ".join(need_clothes)} and will not need {" ".join(unwanted_clothes)}'


class ClosesKind(models.Model):
    name = models.CharField(max_length=100)
    required = models.BooleanField()
    allow_layers = models.BooleanField()


class Clothes(models.Model):
    name = models.CharField(max_length=50)
    allow_rain = models.BooleanField(verbose_name='допускается ношение в дождь')
    allow_snow = models.BooleanField(verbose_name='допускается ношение в снег')
    allow_wind = models.BooleanField(verbose_name='допускается ношение в ветер')
    temp_resist = models.IntegerField()
    kind = models.ForeignKey(ClosesKind, on_delete=models.CASCADE, related_name='clothes', verbose_name='вид одежды')
