import discord
import random
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('----------------')
    now_playing = discord.Game(name='//help')
    await client.change_status(game=now_playing, idle=False)
    

#Server Log when user is banned 
@client.event 
async def on_member_ban(member):
    await client.send_message(discord.Object(id='218732646291734530'), ':no_entry: User **{}** has been **banned** from the server'.format(member))

#Server Log when user is unbanned 
@client.event
async def on_member_unban(server, user):
    await client.send_message(discord.Object(id='218732646291734530'), ':white_check_mark: User **{}** has been **unbanned** from the server'.format(user))


#Message and log when member leaves 
@client.event
async def on_member_remove(member):
    server = member.server
    await client.send_message(server, '{0.mention} has left **{1.name}**'.format(member, server))
    await client.send_message(discord.Object(id='218732646291734530'), ':warning: User {} has left the server' .format(member))

#Message and log when user joins the server 
@client.event
async def on_member_join(member):
    server = member.server
    await client.send_message(server, 'Welcome, {0.mention} to the one and only **{1.name}**! You can now succesfully *smash* *pussy* 😉!'.format(member, server))
    await client.send_message(discord.Object(id='218732646291734530'), ':warning: User {} has joined the server' .format(member))


#Commands and functions 
@client.event
async def on_message(message):

    '''
    Example messasge:

    elif message.content.startswith('//example'):
     msg = await client.send_message(message.channel, 'example')
    '''

    if message.content.startswith('//test'):
      msg = await client.send_message(message.channel, 'hello world')

    elif message.content.startswith('bepis bot is shit'):
        msg = await client.send_message(message.channel, 'what the fuck did you just say about me, you little bitch?')

    elif message.content.startswith('succ'):
         msg = await client.send_message(message.channel, '*succ*')

    elif message.content.startswith('rawr'):
         msg = await client.send_message(message.channel, 'XD')

    elif message.content.startswith('//help'):
        member = message.author
        with open('help.txt', 'r') as help:
         msg = await client.send_message(member, help.read())

#Token
client.run('token')

#notes
##https://discordapp.com/oauth2/authorize?client_id=218513652683243520&scope=bot&permissions=536345663 
