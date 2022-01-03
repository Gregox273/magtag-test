"""
Gregory Brooks 2021
"""

# from adafruit_magtag.magtag import MagTag
import alarm
import board
import time

from octopusenergy import OctopusEnergy
from openweather import OpenWeather

PERIOD_MINUTES = 15

def run(instance):
    instance.network.connect()

    try:
        instance.fetch()
    except (ValueError, RuntimeError) as e:
        print(e)

def run_open_weather_map():
    open_weather_map = OpenWeather()
    run(open_weather_map)

def run_octopus_energy():
    octopus_energy = OctopusEnergy()
    run(octopus_energy)

def main():
    wake_alarm = alarm.wake_alarm
    buttons = (board.BUTTON_A, board.BUTTON_B)
    pin_alarms = [alarm.pin.PinAlarm(pin=pin, value=False, pull=True)
        for pin in buttons]

    if hasattr(wake_alarm, "pin"):
        if wake_alarm.pin == board.BUTTON_B:
            run_octopus_energy()
        else:
            run_open_weather_map()
    else:
        run_open_weather_map()

    time_alarm = alarm.time.TimeAlarm(
        monotonic_time=int(time.monotonic()) + (60 * PERIOD_MINUTES))
    alarm.exit_and_deep_sleep_until_alarms(time_alarm, *pin_alarms)

main()
