# © mat 2020
import discord
from bot_token import *

bot_user_id = 681980762903543902 #Bot's unique user id
channel_id_list = 682050301263478802

client = discord.Client()

print("-------\nBot is live\nUse control+C to terminate\n-------")

@client.event
async def on_message(message):

    #print all messages
    print(message.author,"-",message.content)

    channel = message.channel
    message_sender = message.author.mention

    #play command reminder
    playCommands = ["/play", "//play", "!play", "?play"]
    if message.content.startswith(tuple(playCommands)):
        if message.channel.id == channel_id_list:
            pass
        else: 
            await channel.send(message_sender+" I think you meant #music-commands , headass.")

    #bruh message
    if "bruh" in message.content:
        if message.author.id == bot_user_id:
            pass
        else:
            await channel.send("bruh")

client.run(discord_bot_token)

#API: https://discordpy.readthedocs.io/en/latest/

'''Todo: 
    allow channel id to be a list
    link desired channel in reply
'''
