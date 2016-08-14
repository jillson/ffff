import sys
import requests

baseURL = "http://api.fantasy.nfl.com/v1/players/weekstats"

url = baseURL + "?season=2015&week=1"

r = requests.get(url)

with open("sample.json","wt") as f:
    f.write(str(r.content))

