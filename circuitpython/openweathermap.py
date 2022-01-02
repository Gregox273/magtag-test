"""
Gregory Brooks 2021
"""

from adafruit_magtag.magtag import MagTag
from secrets import secrets

KELVIN_CELSIUS = 273.15

DATA_SOURCE = "https://api.openweathermap.org/data/2.5/weather?"\
    "q=Cambridge,uk"\
    f"&appid={secrets['openweathermap-api-key']}"

DATA_LOCATIONS = (
    ["weather", 0, "icon"],
    ["main", "temp"],
    ["main", "pressure"],
    ["main", "humidity"],
    ["wind", "speed"],
    ["wind", "deg"],
    ["clouds", "all"],
)

class OpenWeatherMap:
    def __init__(self):
        self.magtag = MagTag(
            url=DATA_SOURCE,
            json_path=DATA_LOCATIONS,
        )

        # Weather Icon
        self.magtag.add_text(
            text_position=(10, 15),
            text_transform=lambda x: "Icon: {}".format(x),
        )
        # Temperature
        self.magtag.add_text(
            text_position=(10, 30),
            text_transform=\
                lambda x: "Temperature: {}C".format(x-KELVIN_CELSIUS),
        )
        # Pressure
        self.magtag.add_text(
            text_position=(10, 45),
            text_transform=lambda x: "Pressure: {}hPa".format(x),
        )
        # Humidity
        self.magtag.add_text(
            text_position=(10, 60),
            text_transform=lambda x: "Humidity: {}%".format(x),
        )
        # Wind Speed
        self.magtag.add_text(
            text_position=(10, 75),
            text_transform=lambda x: "Wind Speed: {}m/s".format(x),
        )
        # Wind Direction
        self.magtag.add_text(
            text_position=(10, 90),
            text_transform=lambda x: "Wind Direction: {}deg".format(x),
        )
        # Cloudiness
        self.magtag.add_text(
            text_position=(10, 105),
            text_transform=lambda x: "Cloud: {}%".format(x),
        )

    def connect(self):
        self.magtag.network.connect()

    def fetch(self):
        self.magtag.fetch()

    def exit_and_deep_sleep(self, period_seconds):
        self.magtag.exit_and_deep_sleep(period_seconds)
