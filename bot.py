import discord
import asyncio
from discord.ext import commands
import random
from datetime import datetime
import numpy
import configparser

description = 'Daniel Bot: By Daniel'
bot = commands.Bot(command_prefix='?', description=description)
'''client = discord.Client()'''

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='?help'))

@bot.event
async def on_message(message : discord.Message):

    if message.server != None:
        name = 's' + str(message.server.id)
    else:
        name = 'u' + str(message.author.id)

    txtfile = open(name + '.txt', "a")

    print(str(datetime.now())+ ' -> Message recorded in: ' + name)
    content = message.content
    content = content.replace('\n', '/\\')
    txtfile.write(str(message.author.name) + ' | ' + str(message.timestamp) + ' | ' + str(content) + '\n')
    txtfile.close()

    await bot.process_commands(message)

@bot.command(pass_context = True, description = 'Prints stats about a user')
async def stats(ctx, username= '0'):

        user = discord.utils.get(ctx.message.server.members, name=username)

        if  user != None:
            await sayStats(user)
        else:
            await bot.say('Please specify valid user.')

@bot.command(pass_context = True, description = 'Determines who is the coolest person in the server.')
async def whoiscool(ctx):
    user = ctx.message.author.name
    nick = ctx.message.author.nick

    if user == 'PigPen':
        await bot.say(nick + ' is cool.')
    else:
        num = random.randrange(1, 5, 1)
        if num == 1:
            message = nick + ' is a loser.'
        elif num == 2:
            message = nick + ' is not cool.'
        elif num == 3:
            message = 'Not you, loser.'
        elif num == 4:
            message = 'Me. I\'m cool'
        elif num == 5:
            message = nick + ' is not as cool as the jon e character.'
        await bot.say(message)

@bot.command()
async def spampost(spamwords : str, numberofspams : int):
    if numberofspams > 10:
        await bot.say('u cant do that thats illegal')
    else:
        for i in range(0,numberofspams):
            await bot.say(spamwords)

@bot.command(description = 'Outputs the other less cool people in the server.')
async def whoelseiscool():
    await bot.say('Only jon e is cool.')

@bot.command()
async def befriend():
    await bot.say('Lol, look at this loser, trying to be freinds with a computer.')

@bot.command()
async def frendlee():
    await bot.say('用垃圾机器人看看这些输家')

@bot.command()
async def quickmafs(*nums : int):
    ans = 0
    sums = ''
    for num in nums:
        ans += num
        sums += str(num) + ' + '
    sums = sums[:-2] + ' '
    await bot.say(sums + 'is ' + str(ans) + ' - 1' + ' thats ' + str(ans - 1) + ' quick mafs')

@bot.command()
async def doprimes(n : int):
    output = ''
    for i in range(3, n + 1, 2):
        for a in range(1, i + 1, 2):
            if a == i:
                if len(output + str(i) + '\n') > 1999:
                    await bot.say(output)
                    output = ''
                else:
                    output += str(i) + '\n'
            elif i % a == 0 and a != 1:
                break
    await bot.say(output)

@bot.command()
async def temperatureofman():
    await bot.say('Man\'s not hot.')

async def sayStats(user : discord.User):
    stats = '```'
    stats += user.name + '\'s Stats:\n\n'
    stats += 'Nickname: ' + user.nick + '\n'
    stats += 'Created on: ' + str(user.created_at) + '\n'
    stats += 'Joined: ' + str(user.joined_at) + '\n'
    stats += "Roles: "
    for n in user.roles:
        stats += '| ' + n.name + ' |'
    stats += '\n'
    stats += "```"
    await bot.say(stats)

config = configparser.ConfigParser()
config.read('config.ini')
cfg = config['SETTINGS']
token = cfg['token']

bot.run(token)
