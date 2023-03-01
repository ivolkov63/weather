import datetime
import json
import requests


def get_weather_data(lat, lon, key):
    data = requests.get(
        f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=hourly,daily&appid={key}&units=metric')

    json_data = json.loads(data.content.decode())

    return json_data["current"]["temp"], json_data["current"]["weather"]["main"], json_data["current"].get(
        'wind_speed'), json_data["current"].get('wind_gust'), json_data['current']['dt']


def prepare_weather_datetime(dt):
    gmt_time = datetime.datetime.fromtimestamp(dt)
    return gmt_time + 4