import discord
import os
from discord.ext import commands

command_prefix = '!!'
hsbot = commands.Bot(command_prefix=command_prefix)

# Reads the token from file
def read_token():
    with open("token.txt") as token:
        line = token.readlines()
        return line[0].strip()


TOKEN = read_token()

@hsbot.event
async def on_ready():
    print("Bot is ready!")

# get all the cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        hsbot.load_extension(f'cogs.{filename[:-3]}')

hsbot.run(TOKEN)