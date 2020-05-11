import discord
from discord.ext import commands

import mysql.connector
from mysql.connector import errorcode

class Listadd(commands.Cog):

    def __init__(self, hsbot):
        self.hsbot = hsbot

    @commands.command()
    async def addtolist(self, ctx, *args):
        msg = ctx.message.content
        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used) + len(alias_used):]
        splitted_text = text.split(',')

        if text == '':
            await ctx.send(content='You need to specify the text!')
            return

        peli = splitted_text[0].strip()
        pelaajaMaara = splitted_text[1].strip()
        pisteMaara = splitted_text[2].strip()
        pelaaja = splitted_text[3].strip()

        if len(args) != 4:
            embed = discord.Embed(title='', description='väärä määrä')
            await ctx.send(embed=embed)
            pass
        elif (not pelaajaMaara.isnumeric()) or (not pisteMaara.isnumeric()):
            await ctx.send("Muodon pitää olla peli, pelaajamäärä, pisteet, nimimerkki")
            pass
        else:
            try:
                cnx = mysql.connector.connect(user='Skonton', password='KirsikkaPommi500',
                                              host='127.0.0.1',
                                              database='highscorebot')
                cursor = cnx.cursor()

                add_score = ("INSERT INTO highscores "
                             "(PELI, PELAAJAMAARA, PISTEMAARA, PELAAJA) "
                             "VALUES (%s, %s, %s, %s)")

                # peli = splitted_text[0].strip()
                pelaajaMaara = int(splitted_text[1])
                pisteMaara = int(splitted_text[2])
                # pelaaja = splitted_text[3].strip()
                score_data = (peli, pelaajaMaara, pisteMaara, pelaaja)

                cursor.execute(add_score, score_data)

                cnx.commit()

            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print(err)
            else:
                cursor.close()
                cnx.close()
            await ctx.send(content=f"{text}")
            pass
        return

def setup(hsbot):
    hsbot.add_cog(Listadd(hsbot))