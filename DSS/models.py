from django.db import models
from parser_weather.parser import get_weather_data, prepare_weather_datetime

class Clothes(models.Model):
    lat = models.CharField(max_length=10)
    lon = models.CharField(max_length=10)
    key = models.TextField()
    user_clothes = models.TextField()

    def give_recommendation(self):
        lat = self.lat
        lon = self.lon
        key = self.key
        user_clothes = str(self.user_clothes).split()

        temp, weather, wind_speed, wind_gust, dt = get_weather_data(lat, lon, key)
        dt = prepare_weather_datetime(dt)

        if int(wind_gust) > 10 or int(wind_speed) > 10:
            weather_clothes_set = {}            # заполнить значениями {temp: clothes}
            need_clothes = [elem for elem in weather_clothes_set[temp] if elem not in user_clothes]
            unwanted_clothes = [elem for elem in user_clothes if elem not in weather_clothes_set[temp]]
        elif weather == 'rain':
            rainy_clothes_set = {}              # заполнить значениями {temp: clothes}
            need_clothes = [elem for elem in rainy_clothes_set[temp] if elem not in user_clothes]
            unwanted_clothes = [elem for elem in user_clothes if elem not in rainy_clothes_set[temp]]

        else:
            sunny_clothes_set = {}              # заполнить значениями {temp: clothes}
            need_clothes = [elem for elem in sunny_clothes_set[temp] if elem not in user_clothes]
            unwanted_clothes = [elem for elem in user_clothes if elem not in sunny_clothes_set[temp]]

        return f' temperature at {dt} is {temp}. Of the things you have, you will need {" ".join(need_clothes)} and will not need {" ".join(unwanted_clothes)}'