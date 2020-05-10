import discord
from discord.ext import commands

import mysql.connector
from mysql.connector import errorcode

class Printlist(commands.Cog):

    def __init__(self, hsbot):
        self.hsbot = hsbot

    @commands.command()
    async def printList(self, ctx):
        cnx = mysql.connector.connect(user='x', password='x',
                                      host='x',
                                      database='highschorebot')
        cursor = cnx.cursor()

        query = ("SELECT PELI, PELAAJAMAARA, PISTEMAARA, PELAAJA FROM highscores "
                 "ORDER BY PISTEMAARA DESC LIMIT 3")

        cursor.execute(query)
        results = cursor.fetchall()

        for r in results:
            print(r)
            await ctx.send(r)

def setup(hsbot):
    hsbot.add_cog(Printlist(hsbot))