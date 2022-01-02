"""
Gregory Brooks 2021
"""

# from adafruit_magtag.magtag import MagTag
from openweathermap import OpenWeatherMap

open_weather_map = OpenWeatherMap()

open_weather_map.connect()

try:
    open_weather_map.fetch()
    open_weather_map.exit_and_deep_sleep(60 * 30)
except (ValueError, RuntimeError) as e:
    print(e)