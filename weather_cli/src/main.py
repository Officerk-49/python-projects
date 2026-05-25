import os
import sys
from dotenv import load_dotenv
from fetch import fetch_weather
from display import display_weather

load_dotenv()

api_key = os.getenv('API_KEY')

def read_stdin():
    try:
        city = sys.argv[1]
        return city
    except IndexError:
        sys.exit('City field is Empty!')

city = read_stdin()
data = fetch_weather(city, api_key)

display_weather(data)

