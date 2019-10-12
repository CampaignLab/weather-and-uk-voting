import os
import json
import glob
import numpy as np
from collections import defaultdict
from tqdm import tqdm
from darksky import forecast
from datetime import datetime

key = os.environ['DARKSKY_KEY']
saved_weather_fns = glob.glob('weather-data-output/*/*.json')
saved_weather = defaultdict(list)

for fn in saved_weather_fns:
    t = fn.split('/')[1]
    lat = float(fn.split('/')[2].split('_')[-2])
    long = float(fn.split('/')[2].split('_')[-1][:-5])
    saved_weather[t].append([lat, long])


def dump_weather_for_t(t: datetime = datetime(year=2018, month=5, day=3).isoformat(),
                       location: tuple = (42.36, -71.05),
                       dry_run=True):
    if not os.path.isdir(f'weather-data-output/{t}'):
        os.makedirs(f'weather-data-output/{t}')

    needs_new_request = False

    if len(saved_weather[t]) > 0:
        dists = np.linalg.norm(np.array(saved_weather[t]) - np.array(location), axis=1)
        dist_min_ind = np.argmin(dists)

        try:
            dist_min = dists[dist_min_ind]
        except IndexError:
            dist_min = dists  # just one entry

        if dist_min > 1:  # 0.1deg is about 7 miles
            needs_new_request = True
    else:
        needs_new_request = True

    if not needs_new_request:
        coords_cached = saved_weather[t][dist_min_ind]
        out_filename = f'weather-data-output/{t}/{coords_cached[0]}_{coords_cached[1]}.json'
    elif needs_new_request and not dry_run:
        out = forecast(key, latitude=location[0], longitude=location[1], time=t)
        out_filename = f'weather-data-output/{t}/{location[0]}_{location[1]}.json'

        with open(out_filename, 'w') as f:
            json.dump(out['hourly'], f)

        saved_weather[t].append([location[0], location[1]])

    return out_filename


if __name__ == '__main__':
    dump_weather_for_t(dry_run=True)
