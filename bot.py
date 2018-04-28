import discord
import random
from discord.ext import commands
from riotwatcher import RiotWatcher


my_region = 'na1'

# DO NOT UPLOAD THIS TOKEN
TOKEN = ''
watcher = RiotWatcher('')

# intial greeting functionality
# command prefix so that the bot looks at the message

bot = commands.Bot(command_prefix='$', description='A bot that greets the user back.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
	await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def say(ctx, userinput: str):
	await ctx.send(userinput)

@bot.command()
async def roll(ctx, dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

#################### RIOT API ##################
# takes summoner name as a param

@bot.command()
async def lol(ctx, summoner_name):
    summoner = watcher.summoner.by_name(my_region, summoner_name)
    sending_str = ''

    for v in summoner:
        sending_str += "%s - %s \n"%(v, summoner[v])
    print(summoner)
    
    filters = ('inactive', 'freshBlood', 'veteran', 'playerOrTeamId', 'playerOrTeamName', 'leagueId', 
        'hotStreak', 'leagueName')
    ranked_stats = watcher.league.positions_by_summoner(my_region, summoner['id'])
   
    for r in ranked_stats:
        sending_str += "\n"
        for v in r:
            if v in filters:
                continue
            sending_str += "%s - %s \n"%(v, r[v])
    await ctx.send(sending_str)
   
bot.run(TOKEN)
