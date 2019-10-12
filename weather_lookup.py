import os
import json
from darksky import forecast
from datetime import datetime

key = os.environ['DARKSKY_KEY']


def dump_weather_for_t(t: datetime = datetime(year=2018, month=5, day=3).isoformat(),
                       locations: tuple = ((42.36, -71.05),),
                       dry_run=True):
    for loc in locations:
        if not dry_run:
            out = forecast(key, loc[0], loc[1], time=t)

    out_filename = f'weather-data-output/{t}-{loc}.json'
    with open(out_filename, 'w') as f:
        json.dump(out['hourly'], f)

    return out_filename


if __name__ == '__main__':
    dump_weather_for_t()
