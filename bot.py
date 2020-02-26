# © mat 2020
#https://github.com/MatRanc/saucy-bot
import discord
from bot_token import *

#Bot's unique user id
bot_user_id = 681980762903543902
#Unique id for music channel
music_channel_id = 682050301263478802

client = discord.Client()

print("-------\nBot is live\nUse control+C to terminate\n-------")

@client.event
async def on_message(message):

    #print all messages
    print(message.author,"-",message.content)

    channel = message.channel
    message_sender = message.author.mention
    music_channel = client.get_channel(music_channel_id)

    #play command reminder
    playCommands = ["/play", "//play", "!play", "?play"]
    if message.content.startswith(tuple(playCommands)):
        if message.channel.id == music_channel_id:
            pass
        else: 
            await channel.send(message_sender+" I think you meant "+music_channel.mention+" , headass.")

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
'''
