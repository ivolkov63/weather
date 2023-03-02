import datetime
import json

import requests

WEATHER_KEY = "a913820bf489df63e3c2055d0916cbfe"

def get_weather_data(lat, lon, key):
    data = requests.get(
        f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=hourly,daily&appid={key}&units=metric')

    json_data = json.loads(data.content.decode())
    try:
        return json_data["current"]["temp"], json_data["current"]["weather"]["main"], json_data["current"].get(
            'wind_speed'), json_data["current"].get('wind_gust'), json_data['current']['dt']
    except KeyError:
        return -4, 'sunny', 3, 5, datetime.datetime.now().timestamp()


def prepare_weather_datetime(dt):
    gmt_time = datetime.datetime.fromtimestamp(dt)
    return gmt_time + datetime.timedelta(hours=4)
