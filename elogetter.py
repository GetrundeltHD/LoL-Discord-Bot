# -*- coding: utf-8 -*-

import urllib.request, json

# Created by GetrundeltHD
# 12-11-2017

"""
If you use this code for a public discord server you have to make
sure to use a proper riot api key!
DONT use a development api key!

"""

def getElo(name = ""):

    if name == "":
        return "nothing", "nothing"

    API_KEY = "YOUR API KEY" # get a proper api key
    URL1 = "https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + name + "?api_key=" + API_KEY

    # encode name for the api request (only some characters)
    URL1 = URL1.replace(u"Ü", "%C3%9C")
    URL1 = URL1.replace(u"ü", "%C3%9C")
    URL1 = URL1.replace(u"µ", "%C2%B5")
    URL1 = URL1.replace(u" ", "%20")
    URL1 = URL1.replace(u"Ä", "%C3%84")
    URL1 = URL1.replace(u"ä", "%C3%84")
    URL1 = URL1.replace(u"Ö", "%C3%96")
    URL1 = URL1.replace(u"ö", "%C3%96")

    try:
        headers = {}
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
        headers["Origin"] = "https://developer.riotgames.com"
        headers["Accept-Charset"] = "application/x-www-form-urlencoded; charset=UTF-8"
        headers["X-Riot-Token"] = API_KEY
        headers["Accept-Language"] = "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"

        # API-Call to get the summoner-id
        # for the given summoner-name
        req = urllib.request.Request(URL1, headers=headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read().decode("utf-8", "strict")

        sum_id = json.loads(respData)["id"]
        
        URL_2 = "https://euw1.api.riotgames.com/lol/league/v3/leagues/by-summoner/" + str(sum_id) + "?api_key=RGAPI-5c014afd-d8a8-4b9d-bfc5-f7e825071b9e"

        # API-Call to get the ranked data
        # for the given summonerid
        req = urllib.request.Request(URL_2, headers=headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read().decode("utf-8")

        # decode data
        temp = json.loads(respData)

        a_of_sums = temp[0]["entries"]

        # get elo from dict
        elo = temp[0]["tier"]

        # serch for key that similar to the given username
        for summ in a_of_sums:
            if summ["playerOrTeamName"] == name:
                summoner = summ
                
        if summoner == None:
            return None, None
    
        return(elo, summoner)

    except:
        return None, None
    
