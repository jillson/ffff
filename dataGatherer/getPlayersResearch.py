import sys
import requests

baseURL = "http://api.fantasy.nfl.com/v1/players/researchinfo?format=json"


def getPlayersByOffset(weekURL):
    pdata = []
    offset = 0
    while True:
        url = weekURL + "&offset=" + str(offset)
        r = requests.get(url)
        data = r.json()
        if not data.get("players") or len(data["players"]) <= 0:
            break
        pdata += data["players"]
        offset += 50
    return pdata


for week in range(18):
    weekurl = baseURL + "&week=%d&season=2015" % week
    data = getPlayersByOffset(weekurl)
        
    with open("tempdata/2015/%d/research.json" % week,"wt") as f:
        f.write(str(data))

