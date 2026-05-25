from utils import country_convert

def display_weather(info):
    temp = info['main']['temp']
    city = info['name']
    country = country_convert(info['sys']['country'])
    description = info['weather'][0]['main']
    wind = info['wind']['speed']

    print('-----------------------------------------')
    print(f"{'Weather':^41}")
    print('-----------------------------------------')
    print(f'{'Temperature':<15} : {round(temp)} °C')
    print(f'{'City':<15} : {city}')
    print(f'{'Country':<15} : {country}')
    print(f'{'Description':<15} : {description}')
    print(f'{'Wind':<15} : {wind} km/h')
    print('-----------------------------------------')
