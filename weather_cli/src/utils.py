import pycountry

def country_convert(code):
    country = pycountry.countries.get(alpha_2=code).name
    return country if country else "Unknown"
