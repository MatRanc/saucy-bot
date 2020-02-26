# © mat 2020
import discord
from bot_token import *

client = discord.Client()

print("Bot is live\nUse control+C to terminate")

@client.event
async def on_message(message):

    channel = message.channel
    messageSender = message.author.mention

    print(message.author,"-",message.content)
    if message.content.startswith("/play"):
            if message.channel.name == "music-commands":
                print("OK")
            else: 
                await channel.send(messageSender+" I think you meant #music-commands, headass.")

client.run(discord_bot_token)