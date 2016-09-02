import discord
from discord.ext import commands
import random
import asyncio
import datetime
from random import randint




client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('----------------')
    now_playing = discord.Game(name='>help')
    await client.change_status(game=now_playing, idle=False)




#Random number gen, with capabilities for trips and quads
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)




@client.event
async def on_message(message):

    '''
    Example messasge:

    elif message.content.startswith('>example'):
     msg = await client.send_message(message.channel, 'example')
    '''


    if message.content.startswith('>test'):
      msg = await client.send_file(message.channel, 'helloworld.jpg')



    elif message.content.startswith('>help'):
        member = message.author
        with open('help.txt', 'r') as help:
         msg = await client.send_message(member, help.read())


    elif message.content.startswith('>roll'):
        msg = await client.send_message(message.channel, random_with_N_digits(9)) 


    elif message.content.startswith('>dev'):
        member = message.author
        with open('details.txt', 'r') as develop:
         msg = await client.send_message(member, develop.read())


    elif message.content.startswith('>tits'):
        await client.send_file(message.channel, 'tits.jpg')

    elif message.content.startswith('>father'):
        await client.send_file(message.channel, 'father.jpg')


#Token
client.run('Insert_Token_Here')