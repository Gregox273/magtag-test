"""
Gregory Brooks 2021
"""

# from adafruit_magtag.magtag import MagTag
import alarm

from octopusenergy import OctopusEnergy
from openweather import OpenWeather

def run(instance):
    instance.network.connect()

    try:
        instance.fetch()
        instance.exit_and_deep_sleep(60 * 30)
    except (ValueError, RuntimeError) as e:
        print(e)

def run_open_weather_map():
    open_weather_map = OpenWeather()
    run(open_weather_map)

def run_octopus_energy():
    octopus_energy = OctopusEnergy()
    run(octopus_energy)

if alarm.sleep_memory[0] > 0:
    alarm.sleep_memory[0] = 0
    run_open_weather_map()
else:
    alarm.sleep_memory[0] = 1
    run_octopus_energy()

