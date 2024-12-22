import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')


@dataclass
class WeatherData:
    main:str
    description: str
    icon: str
    temperature: float

def get_lan_lon( city_name, state_code, country_code, API_key):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    data = resp[0]
    lat, lon = data.get('lat'), data.get('lan')
    return lat, lon

def get_current_weather(lat, lon, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIkey}&units=metric').json()
    data = WeatherData(
        main=resp.get('weather')[0].get('main',)
        description=resp.get('weather')[0].get('description',)
        icon=resp.get('weather')[0].get('icon',)
    )

if __name__ == "__main__":



    