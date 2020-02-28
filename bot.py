# © mat 2020
#https://github.com/MatRanc/saucy-bot
import discord
from bot_token import *

#Bot's unique user id
bot_user_id = 681980762903543902

#Unique id for music channel
music_channel_id = 532321197988511744
#682050301263478802 = test server
#532321197988511744 = main

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
    playCommands = ["/play", "//play", "!play", "?play", "/skip", "/queue"]
    if message.content.startswith(tuple(playCommands)):
        if message.channel.id != music_channel_id:
            await message.delete()
            await channel.send(message_sender+" Please use "+music_channel.mention+" for music commands.")

    #delete bot messages
    if message.channel.id != music_channel_id:
        if message.author.name == "Rythm":
            await message.delete()

    #bruh message
    if "bruh" in message.content:
        if message.author.id == bot_user_id:
            pass
        else:
            await channel.send("bruh")

#Check for bot token
if not discord_bot_token:
    print("ERROR: A bot token is required to run.\nPlease get one from the Discord Developer Portal")
    sys_exit()

#run
client.run(discord_bot_token)

#API used: https://discordpy.readthedocs.io/en/latest/

'''Todo:
    allow channel id to be a list
    make music channel id collection based off name
'''
