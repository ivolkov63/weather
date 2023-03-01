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


#def func(array):
#    sum_array = []
#    num = 0
#    for item1 in enumerate(array):
#        for item2 in enumerate(array):
#            if item2[0] <= item1[0]:
#                continue
#            for item3 in enumerate(array):
#                if item3[0] <= item2[0]:
#                    continue
#                sum_array.append(item1[1] + item2[1] + item3[1])
#        num += 1
#
#    return sum_array
#
#
#def func2(array, target):
#    array.append(target)
#    array = sorted(array)
#    if array.count(target) > 1:
#        return target
#    if array[0] == target:
#        return array[1]
#    if array[-1] == target:
#        return array[-2]
#    if target - array[array.index(target) - 1] < array[array.index(target) + 1] - target:
#        return array[array.index(target) - 1]
#    else:
#        return array[array.index(target) + 1]
#
#
#def func3(array, target):
#    return func2(func(array), target)