import os
import requests
import sys
import json
import pytemperature

def get_weather(api_key, city, country):
    erqrew
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}"
    res = requests.get(url)
    result = res.json()
    y = result['main']
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = result["weather"]
    weather_description = z[0]["description"]

    print(" Temperature (in Kelvin) = " +
            str(current_temperature) +
            "\n Temperature (in Celsius) = " +
            str(pytemperature.k2c(current_temperature)) +
            "\n Temperature (in Farenheit) = " +
            str(pytemperature.k2f(current_temperature)) +
            "\n atmospheric pressure (in hPa unit) = " +
            str(current_pressure) +
            "\n humidity (in percentage) = " +
            str(current_humidity) +
            "\n description = " +
            str(weather_description))


