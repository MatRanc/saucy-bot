# © mat 2020
import discord
from bot_token import *

client = discord.Client()

@client.event
async def on_message(message):

    channel = message.channel
    messageSender = message.author.mention

    print(message.author,"-",message.content)
    if message.content.startswith("/play"):
            await channel.send(messageSender+" I think you meant #music-commands, headass.")

client.run(discord_bot_token)