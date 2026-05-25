import sys
import requests

def fetch_weather(city, api_key):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
            }
    response = requests.get(url, params=params)
    data = response.json()
    if int(data['cod']) != 200:
        message = data['message']
        sys.exit(f'{message}')
    return data
