import discord
from discord.ext import commands

import mysql.connector
from mysql.connector import errorcode


class Printlist(commands.Cog):

    def __init__(self, hsbot):
        self.hsbot = hsbot

    @commands.command()
    async def printList(self, ctx, peli : str = None):
        cnx = mysql.connector.connect(user='Skonton', password='KirsikkaPommi500',
                                      host='127.0.0.1',
                                      database='highscorebot')
        cursor = cnx.cursor()
        if peli != None:
            query = ("SELECT PELI, PELAAJAMAARA, PISTEMAARA, PELAAJA FROM highscores "
                     "WHERE PELI = %s"
                     "ORDER BY PISTEMAARA DESC LIMIT 3")
            spel = peli
            cursor.execute(query, (spel,))
        else:
            query = ("SELECT PELI, PELAAJAMAARA, PISTEMAARA, PELAAJA FROM highscores "
                     "ORDER BY PISTEMAARA DESC LIMIT 3")
            cursor.execute(query)

        results = cursor.fetchall()
        for r in results:
            print(r)
            await ctx.send(r)

def setup(hsbot):
    hsbot.add_cog(Printlist(hsbot))