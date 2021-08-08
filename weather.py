import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--city", help="天気を知りたい町を指定します")
args = parser.parse_args()

city = ''
if args.city:
    city = args.city

params = {'lang': 'ja', 'format': 'j1'}

r = requests.get('https://wttr.in/' + city, params=params)
weather = r.json()
print(
    '{0}の現在の天気: {1}'.format(
        weather['nearest_area'][0]['areaName'][0]['value'],
        weather['current_condition'][0]['lang_ja'][0]['value'],
    )
)
