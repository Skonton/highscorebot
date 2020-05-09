import discord
from discord.ext import commands

class Listadd(commands.Cog):

    def __init__(self, hsbot):
        self.hsbot = hsbot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong :)")


def setup(hsbot):
    hsbot.add_cog(Listadd(hsbot))