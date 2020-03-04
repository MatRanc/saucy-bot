# © mat 2020
#https://github.com/MatRanc/saucy-bot
import discord
import random
from bot_token import token_string

#Bot's unique user id
bot_user_id = 681980762903543902
#Unique id for music channel
music_channel_id = 532321197988511744
#682050301263478802 = test server
#532321197988511744 = main
say_channel_id = 683191210302504990
#683191210302504990 = say channel on saucyclub
general_channel_id = 248966523190771714
#248966523190771714 = general channel on saucyclub

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

    #repeat anything said in #say to #general as bot
    if message.channel.id == say_channel_id:
        if message.content.startswith("IGNORE"):
            pass
        else:
            general_channel = client.get_channel(general_channel_id)
            await general_channel.send(message.content)

    #eight ball
    eightball_prompts = ["is", "Is", "8ball"]
    eightball_responses = ["Yes", "No", "Probably", "No way", "Yessir", "Not a chance", "idk ask obama", "bruh really", "Nope", "Keep wishing", "All truth is relative :flushed:", "brb commiting a mass genocide", "is israel a legitimate state?", "According to my sources, yes.", "It seems as though the only logical answer is yes."]
    if message.channel.id != music_channel_id:
        if message.content.startswith(tuple(eightball_prompts)):
            await channel.send(random.choice(eightball_responses))

    #if message contains, ping
    if "jacob" in message.content:
        if message_sender != bot_user_id:
            jacob = client.get_user(330462798817656847) #inset user id for person you want to ping
            await channel.send(jacob.mention) #mention that person

    #send now playing dont care for certain people
    if message.author.id == 330462798817656847:
        if random.randint(1,3) == 1:
            await channel.send("now ᴘʟᴀʏɪɴɢ: Who Asked (Feat: Nobody Did) ───────────:white_circle:────── ◄◄⠀▐▐⠀►► 𝟸:𝟷𝟾 / 𝟹:𝟻𝟼⠀───○ :loud_sound:")
        #print that the user(+tag) did not trigger the message
        else: print("user "+message.author.name+"#"+message.author.discriminator+" did not trigger the \"who asked\" function")

    #swag meter
    swag_prompts = ["how swag is", "How swag is"]
    random_number_1_100 = str(random.randint(1, 100))
    if message.content.startswith(tuple(swag_prompts)):
        await channel.send("swag meter says "+random_number_1_100+"% swag :sunglasses:")

#Check for bot token
if not token_string:
    print("ERROR: A bot token is required to run.\nPlease get one from the Discord Developer Portal")
    sys_exit()

#run
client.run(token_string)

#API used: https://discordpy.readthedocs.io/en/latest/

'''
    Todo:
    -allow channel id to be in a list (so that you cant only have one channel for ignoring messages)
    -make music channel id collection based off name and not channel id
    -add different emojis for swag ratings
'''
