import csv
import json

from tqdm import tqdm
from datetime import datetime

from weather_lookup import dump_weather_for_t

id_to_weather_fn = {}
id_to_name = {}


with open('geography-data/Wards_December_2018_Super_Generalised_Clipped_Boundaries_GB.csv') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)  # skip header

    for row in tqdm(reader):
        objectid = row[0]
        id = row[1]
        name = row[2]
        longitude = float(row[6])
        latitude = float(row[7])

        weather_filename = dump_weather_for_t(t=datetime(year=2017, month=6, day=8).isoformat(),
                                              location=(latitude, longitude),
                                              dry_run=False)

        id_to_weather_fn[id] = weather_filename
        id_to_name[id] = name

    with open('map-id-to-weather.json', 'w') as f_js:
        json.dump(id_to_weather_fn, f_js)

    with open('map-id-to-name.json', 'w') as f_js:
        json.dump(id_to_name, f_js)
