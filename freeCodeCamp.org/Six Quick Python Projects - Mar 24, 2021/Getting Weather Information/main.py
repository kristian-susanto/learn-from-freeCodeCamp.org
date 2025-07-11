# pip install requests
# https://home.openweathermap.org/api_keys
import requests
from pprint import pprint

API_Key = 'your_api_key'

city = input('Enter a city: ')

base_url = 'http://api.openweathermap.org/data/2.5/weater?appid=' + API_Key + '&q=' + city

weather_data = requests.get(base_url).json()

print(weather_data)