import discord
from discord.ext import commands

command_prefix = '!!'
bot = commands.Bot(command_prefix=command_prefix)


@bot.event
async def on_ready():
    print("Bot is ready!")

bot.run('NzA4NzA4MzYyMDM1OTIwOTE3.Xrbm7Q.kQpmDP_rzUWKlmup1Z5bkPeXN4M')