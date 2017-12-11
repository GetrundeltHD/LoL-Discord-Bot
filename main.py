import discord
from discord.ext import commands
import random, elogetter

# Created from GetrundeltHD
# 12-11-2017

"""
If you to use the code you have to download the python module discord.py.
If you are on windows just enter (pip install --user discord.py) in
your command prompt and the download will start.
On mac and linux it will be sightly different.
-----------------------------------------------------------------------
This code is public so you can use it for your private or public
discord. You have to make sure that you have a proper riot api key
in the elogetter module. DONT use the bot with a development api key!

"""

description = "This bot is able to get the elo of a given summoner. -> #summoner <name>"

bot = commands.Bot(command_prefix='#', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    for s in bot.servers:
        print("Connected to: {0} with id: {1}!".format(s.name, s.id))
    
@bot.command()  
async def summoner(*name):
    s = ""
    for i in range(len(name)):
        if(i < len(name) - 1):
            s += name[i] + " "
        else:
            s += name[i]
    print(s)
    elo, summ = elogetter.getElo(s)
    if summ == None or elo == None:
        await bot.say("An error occured!")
    elif summ == "nothing" or elo == "nothing":
        await bot.say("Please enter a summoner name! -> #summoner <name>")
    else:
        out = "The player " + s + " is currently in -> "
        out += elo + " " + summ["rank"] + "\n"
        out += "LP: " + str(summ["leaguePoints"]) + "\n"
        out += "W: " + str(summ["wins"]) + " // L:" + str(summ["losses"]) + "\n"
        if(summ["hotStreak"]):
            out += "Veteran: yes"
        else:
            out += "Veteran: no"
        await bot.say(out)


bot.run('YOUR BOT TOKEN')

