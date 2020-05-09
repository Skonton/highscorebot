import discord
from discord.ext import commands

class Printlist(commands.Cog):

    def __init__(self, hsbot):
        self.hsbot = hsbot

def setup(hsbot):
    hsbot.add_cog(Printlist(hsbot))