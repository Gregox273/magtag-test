"""
Gregory Brooks 2022
"""
from secrets import secrets

from adafruit_magtag.magtag import MagTag

DATA_SOURCE = "https://api.octopus.energy/v1/electricity-meter-points/" \
    + f"{secrets['octopus-electricity-mpan']}"\
    + "/meters/"\
    + f"{secrets['octopus-electricity-serial-number']}"\
    + "/consumption/"

DATA_LOCATIONS = ["results"]

def text_transform(result):
    NUM_GROUPS = 6
    POINTS_PER_GROUP = 8
    PRICE_PER_KWH = secrets['octopus-price-per-kwh']
    rtn_string = ""
    for group in range(0, NUM_GROUPS):
        group_sum = 0
        i = group * POINTS_PER_GROUP
        for point in range(0, POINTS_PER_GROUP):
            j = i + point
            consumption = result[j]['consumption']
            group_sum += consumption
        interval_start = result[j]['interval_start']
        cost = group_sum * PRICE_PER_KWH
        rtn_string += f"{interval_start} : {group_sum}kWh ({cost}p)\n"
    return rtn_string

class OctopusEnergy(MagTag):
    def __init__(self):
        b64_auth = secrets['octopus-api-key-b64']

        super().__init__(
            url=DATA_SOURCE,
            headers={"Authorization": "Basic " + b64_auth},
            json_path=DATA_LOCATIONS,
        )

        self.add_text(
            text_position=(10, 60),
            text_transform=text_transform
        )
