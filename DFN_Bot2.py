import discord
import asyncio
import aiohttp
import json
import random
import requests
from discord import Game
from discord.ext.commands import Bot


BOT_PREFIX = ("?" , "!")
TOKEN = 'Secret ;) '
client = Bot(command_prefix=BOT_PREFIX)

diamondList = []
platList = []
goldList = []
silverList = []
bronzeList = []





@client.event
async def on_ready():
    await client.change_presence(game=Game(name="med livene deres"))
    print("Logged in as " + client.user.name)


@client.command(description='Hva er siste pris per BTC?')
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await client.say("Prisen per Bitcoin er: $ " + value + ".")

@client.command()
async def joined(member : discord.Member):
    await bot.say('Velkommen til vårt nye medlem mr. {0.name}! Som joina  {0.joined_at}'.format(member))


@client.command()
async def getRank(n1, *vartuple):
    name = n1
    for var in vartuple:
        name += var

    url = 'https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + name + '?api_key=RGAPI-c585b94c-d9ac-4b1a-9490-b964f8200159'
    response = requests.get(url)

    try:
        summonerId = response.json()['id']
    except:
        await client.say("Summoner " + name + " does not exist. ")

    #await client.say("Summoner id for " + n1 +" "+ n2 + " is: " + str(summonerId))
    url2 = 'https://euw1.api.riotgames.com/lol/league/v3/positions/by-summoner/' + str(summonerId)+ '?api_key=RGAPI-c585b94c-d9ac-4b1a-9490-b964f8200159'
    response = requests.get(url2)

    if (len(response.json()) == 2):
        print(url2)
        rank = response.json()[0]['tier'] +  " " + response.json()[0]['rank']
        checkRank(name, rank)
        list()
        await client.say("Rank of Summoner " + name +" is: " + rank)

    else:
        await client.say("Summoner " + name + " is a fucking unranked noob.")





@client.command()
async def leaderboard():
    await client.say(" -----Current Leaderboard-----")
    for var in diamondList:
        await client.say(var + "\n")
    for var in platList:
        await client.say(var + "\n")
    for var in goldList:
        await client.say(var + "\n")
    for var in silverList:
        await client.say(var + "\n")
    for var in bronzeList:
        await client.say(var + "\n")
    await client.say(" ------------------------------")





def checkRank(name, rank):
    print("inside")
    if (rank[:5] == 'BRONZE'):
        bronzeList.append(name + "     " + rank)
    elif ( rank[:6] == 'SILVER'):
        silverList.append(name + "     " + rank)
    elif ( rank[:4] == 'GOLD'):
        goldList.append(name + "     " + rank )
    elif ( rank[:8] == 'PLATINUM'):
        platList.append(name + "     " + rank)
    elif( rank[:7] == 'DIAMOND' ):
        diamondList.append(name + "     " + rank)

def insertRank(name, rank, list):

    if not list:
        list.append(name + "     " + rank)


    else:
        current = 'I';
        for var in list:
            division = rank[len(rank)-3:].replace(" ", "")

            print("Division is: ")
            print(division)





@client.command()
async def kjihl():
    server = client.get_channel('409720205825015810')
    with open('Pics/Lucas.jpg', 'rb') as f:
        await client.send_file(server, f)


@client.command()
async def guess(end, num):

    answer = random.randint(1, int(end))

    if (int(num) == int(answer)):
        if(int(end) >= int(10)):
            server = client.get_channel('409720205825015810')
            with open('Pics/pepe_well_memed.jpg', 'rb') as f:
                await client.send_file(server, f)

        await client.say("Congratulations! The correct answer was: " + str(answer))
    else:
        server = client.get_channel('409720205825015810')
        with open('Pics/pepe_sad.jpg', 'rb') as f:
            await client.send_file(server, f)
        await client.say("Sorry. Correct answer was: " + str(answer) + "\nYou guessed: " + num)


@client.command()
async def chuck():
    url = 'http://api.icndb.com/jokes/random'
    response = requests.get(url)

    joke = response.json()['value']['joke']
    await client.say(joke)



@client.command()
async def yomom():
    url = 'http://api.yomomma.info'
    response = requests.get(url)

    joke = response.json()['joke']
    await client.say(joke)


@client.command()
async def spam(s, num):
    if ( int(num) > 10):
        await client.say("Ikke spam serveren da din drittunge..")
    else:
        for i in range(int(num)):
            await client.say(s)



client.run(TOKEN)
