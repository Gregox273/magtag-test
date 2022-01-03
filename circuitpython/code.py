"""
Gregory Brooks 2021
"""

import time

import alarm
import board
import rtc

from octopusenergy import OctopusEnergy
from openweather import OpenWeather

PERIOD_MINUTES = 15
ILLUMINATE_THRESHOLD = 600
ILLUMINATE_COLOUR = (255, 255, 255)
ILLUMINATE_PERIOD_S = 5

def run(instance, illuminate):
    instance.network.connect()

    try:
        instance.fetch()
    except (ValueError, RuntimeError) as e:
        print(e)

    if illuminate:
        # Illuminate if it is dark
        instance.peripherals.neopixel_disable = False
        if instance.peripherals.light < ILLUMINATE_THRESHOLD:
            instance.peripherals.neopixels.fill(ILLUMINATE_COLOUR)
            time.sleep(ILLUMINATE_PERIOD_S)
        instance.peripherals.neopixel_disable = True

def run_open_weather_map(illuminate=False):
    open_weather_map = OpenWeather()
    open_weather_map.network.get_local_time()
    now = rtc.RTC().datetime
    open_weather_map.set_time(now)
    run(open_weather_map, illuminate)

def run_octopus_energy(illuminate=False):
    octopus_energy = OctopusEnergy()
    run(octopus_energy, illuminate)

def main():
    wake_alarm = alarm.wake_alarm
    buttons = (board.BUTTON_A, board.BUTTON_B)
    pin_alarms = [alarm.pin.PinAlarm(pin=pin, value=False, pull=True)
        for pin in buttons]

    if hasattr(wake_alarm, "pin"):
        # If woken by pin alarm
        if wake_alarm.pin == board.BUTTON_B:
            run_octopus_energy(illuminate=True)
        else:
            run_open_weather_map(illuminate=True)
    else:
        run_open_weather_map()

    time_alarm = alarm.time.TimeAlarm(
        monotonic_time=int(time.monotonic()) + (60 * PERIOD_MINUTES))
    alarm.exit_and_deep_sleep_until_alarms(time_alarm, *pin_alarms)

main()
