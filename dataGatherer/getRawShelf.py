import sys
import requests
import shelve

baseURL = "http://api.fantasy.nfl.com/v1/players/researchinfo?format=json"
baseURL2 = "http://api.fantasy.nfl.com/v1/players/weekstats?format=json"


def getPlayersByOffset(weekURL,key="players"):
    pdata = []
    offset = 0
    while offset < 10000:
        url = weekURL + "&offset=" + str(offset)
        r = requests.get(url)
        data = r.json()
        if not data.get(key) or len(data[key]) <= 0:
            break
        pdata += data[key]
        offset += 50
    return pdata


myshelve = shelve.open("rawData.shelf")
for week in range(18):
    weekurl = baseURL + "&week=%d&season=2015" % week
    data = getPlayersByOffset(weekurl)
    #players = dict([[p["id"],[p["firstName"] + " " + p["lastName"],p["position"]]] for p in data if p["teamAbbr"] == "NE" and p["position"] in ['WR','DEF','RB','TE',"QB","K"]])
    weekurl2 = baseURL2 + "&week=%d&season=2015" % week
    data2 = requests.get(weekurl2).json()["playerStats"]
    myshelve["week%d"%week] = [data,data2]

myshelve.close()
