# LoL-Discord-Bot
A Discord-Bot made in Python3 that shows you the elo of an player.

In the main.py is the specified command and the initilisation of the bot.

In the module elogetter.py there is the function for the request to the riot api
that fetches the data for the as parameter given summoner name.

function getElo(name) -> returns a tupel(eloName, dict)
The eloName is a String that just holds the name of the players elo.
The dict thats returned cotains the players name, rank in the given elo, 
league points, if hes an veteran, if hes in a hodstreak, if hes inactive or if hes freshblood.

To use the bot on your discord just type in the chat -> #summoner \<name\>
