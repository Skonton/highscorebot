import discord
from discord.ext import commands

import mysql.connector
from mysql.connector import errorcode

class Printlist(commands.Cog):

    def __init__(self, hsbot):
        self.hsbot = hsbot

    @commands.command()
    async def printlist(self, ctx, *args):
        await ctx.send(':D')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title='', description=f'Tarkistathan, että on oikea muoto :) Opettele kirjottamaan!')
            await ctx.send(embed=embed)

def setup(hsbot):
    hsbot.add_cog(Printlist(hsbot))