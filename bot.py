# © mat 2020
# https://github.com/MatRanc/saucy-bot
import discord
import random
import datetime
from bot_token import token_string

# Bot's unique user id
bot_user_id = 681980762903543902
# Unique id for music channel
music_channel_id = 532321197988511744
# 682050301263478802 = test server
# 532321197988511744 = main
say_channel_id = 683191210302504990
# 683191210302504990 = say channel on saucyclub
general_channel_id = 248966523190771714
# 248966523190771714 = general channel on saucyclub

client = discord.Client()

print("\nsaucybot v1.0 /// FWD Development\n")
print("-------\nBot is live\nUse control+C to terminate\n-------")


@client.event
async def on_message(message):

    # get time of message
    message_time_hour = str(datetime.datetime.now().time().hour)
    message_time_minute = str(datetime.datetime.now().time().minute)
    message_time_second = str(datetime.datetime.now().time().second)

    # print all messages
    if message.author.id != 155149108183695360:  # ignores dyno bot
        print("["+message_time_hour+":"+message_time_minute+":" +
              message_time_second+"]", message.author, "-", message.content)

    channel = message.channel
    message_sender = message.author.mention
    music_channel = client.get_channel(music_channel_id)

    # play command reminder
    playCommands = ["/play", "//play", "!play",
                    "?play", "/skip", "/queue", "-play", "~play"]
    if message.content.startswith(tuple(playCommands)):
        if message.channel.id != music_channel_id:
            await message.delete()
            await channel.send(message_sender+" Please use "+music_channel.mention+" for music commands.")

    # delete bot messages
    if message.channel.id != music_channel_id:
        if message.author.name == "Rythm":
            await message.delete()

    # bruh message
    if "bruh" in message.content:
        if message.author.id == bot_user_id:
            pass
        else:
            await channel.send("bruh")

    # repeat anything said in #say to #general as bot
    if message.channel.id == say_channel_id:
        if message.content.startswith("say"):
            general_channel = client.get_channel(general_channel_id)
            await general_channel.send(message.content[3:])
        else:
            pass

    # eight ball
    eightball_prompts = ["is ",
                         "8ball "]
    eightball_responses = ["Yes",
                           "No",
                           "Probably",
                           "No way",
                           "Yessir",
                           "Not a chance",
                           "idk ask obama",
                           "Nope",
                           "Keep wishing",
                           "All truth is relative :flushed:",
                           "brb commiting a mass genocide",
                           "is israel a legitimate state?",
                           "According to my sources, yes.",
                           "It seems as though the only logical answer is yes."]
    if message.channel.id != music_channel_id:
        if message.content.lower.startswith(tuple(eightball_prompts)):
            await channel.send(random.choice(eightball_responses))

    # obama 8ball
    obama_prompts = [
        "obama",
        "hey obama",
    ]
    obama_responses = [
        "After consulting with Michelle, I'm going to say yes.", "uhhhhh Change. is never easy! but uhhhhh always possible.",
        "The Middle East is obviously an issue that has plagued the region for centuries. So, yes.",
        "You're absolutely right that John McCain has not talked about my Muslim faith... But to answer your question, no.",
        "There is no reason anyone should own an AR-15, and there is no reason the answer is no.",
        "Yes. Obama Out.\nhttps://media2.giphy.com/media/3o7qDLkrKr034Z3hQI/source.gif",
        "I'm really excited about the prospect of a woman president of the United States, but I'm less excited about that question because the answer is no.",
    ]
    if message.channel.id != music_channel_id:
        if message.content.lower.startswith(tuple(obama_prompts)):
            await channel.send("<:obama2:711101818784055327>")
            await channel.send("\""+random.choice(obama_responses)+"\"")

    # if message contains, ping
    if "jacob" in message.content:
        if message_sender != bot_user_id:
            # inset user id for person you want to ping
            jacob = client.get_user(330462798817656847)
            await channel.send(jacob.mention)  # mention that person

    # send now playing dont care for certain people
    if message.author.id == 330462798817656847:
        if random.randint(1, 50) == 1:
            await channel.send("now ᴘʟᴀʏɪɴɢ: Who Asked (Feat: Nobody Did) ───────────:white_circle:────── ◄◄⠀▐▐⠀►► 𝟸:𝟷𝟾 / 𝟹:𝟻𝟼⠀───○ :loud_sound:")
        # print that the user(+tag) did not trigger the message
        else:
            print("user "+message.author.name+"#"+message.author.discriminator +
                  " did not trigger the \"who asked\" function")

    # swag meter
    swag_prompts = ["how swag", "How swag"]
    swag_random_number = random.randint(1, 101)
    if message.content.startswith(tuple(swag_prompts)):
        # 0-20
        if 20 >= swag_random_number >= 0:
            await channel.send("swag meter says "+str(swag_random_number)+"% swag :face_vomiting:")
        # 21-40
        if 40 >= swag_random_number >= 21:
            await channel.send("swag meter says "+str(swag_random_number)+"% swag :grimacing:")
        # 41-60
        if 60 >= swag_random_number >= 41:
            await channel.send("swag meter says "+str(swag_random_number)+"% swag :pensive:")
        # 61-80
        if 80 >= swag_random_number >= 61:
            await channel.send("swag meter says "+str(swag_random_number)+"% swag :sunglasses:")
        # 81-100
        if 100 >= swag_random_number >= 81:
            await channel.send("swag meter says "+str(swag_random_number)+"% swag :partying_face:")
        if 101 == swag_random_number:
            await channel.send("swag meter says "+str(swag_random_number)+"% swag :pog:")

# Check for bot token
if not token_string:
    print("ERROR: A bot token is required to run.\nPlease get one from the Discord Developer Portal")
    sys_exit()

# run
client.run(token_string)

# API used: https://discordpy.readthedocs.io/en/latest/

'''
    Todo:
    -allow channel id to be in a list (so that you cant only have one channel for ignoring messages)
    -make music channel id collection based off name and not channel id
'''
