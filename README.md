# Analysis of how weather affects voting in the UK
> Does weather affect vote share for progressive parties in elections?

## Plan
Use DarkSky Weather API to get weather data for recent election result datasets.

Analyse -- start simple, just correlate turnout and vote share. Later look into confounds, etc.

## Usage
To get weather data:
`DARKSKY_KEY=<your-api-key-here> python extract_ward_latlong.py`
