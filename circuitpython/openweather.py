"""
Gregory Brooks 2021
"""

from secrets import secrets

from adafruit_magtag.magtag import MagTag

KELVIN_CELSIUS = 273.15

DATA_SOURCE = "https://api.openweathermap.org/data/2.5/weather?"\
    "q=Cambridge,uk"\
    f"&appid={secrets['openweather-api-key']}"

DATA_LOCATIONS = (
    ["weather", 0, "icon"],
    ["main", "temp"],
    ["main", "pressure"],
    ["main", "humidity"],
    ["wind", "speed"],
    ["wind", "deg"],
    ["clouds", "all"],
)

class OpenWeather(MagTag):
    def __init__(self):
        super().__init__(
            url=DATA_SOURCE,
            json_path=DATA_LOCATIONS,
        )

        # Weather Icon
        self.add_text(
            text_position=(10, 15),
            text_transform=lambda x: "Icon: {}".format(x),
        )
        # Temperature
        self.add_text(
            text_position=(10, 30),
            text_transform=\
                lambda x: "Temperature: {}C".format(x-KELVIN_CELSIUS),
        )
        # Pressure
        self.add_text(
            text_position=(10, 45),
            text_transform=lambda x: "Pressure: {}hPa".format(x),
        )
        # Humidity
        self.add_text(
            text_position=(10, 60),
            text_transform=lambda x: "Humidity: {}%".format(x),
        )
        # Wind Speed
        self.add_text(
            text_position=(10, 75),
            text_transform=lambda x: "Wind Speed: {}m/s".format(x),
        )
        # Wind Direction
        self.add_text(
            text_position=(10, 90),
            text_transform=lambda x: "Wind Direction: {}deg".format(x),
        )
        # Cloudiness
        self.add_text(
            text_position=(10, 105),
            text_transform=lambda x: "Cloud: {}%".format(x),
        )
