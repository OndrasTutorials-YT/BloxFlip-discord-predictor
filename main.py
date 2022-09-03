import os
import cloudscraper, requests
import discord, time
import random, threading
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())
scraper = cloudscraper.create_scraper(browser={'custom': 'ScraperBot/1.0'})


@bot.command()
async def predict(ctx):
    games = scraper.get("https://rest-bf.blox.land/games/crash").json()
    if ctx.author.id != bot.user.id:
        await ctx.reply(embed=discord.Embed(description="Check your direct messages! - Rocket Predictor 🚀",
                                            color=0x5ca3ff))
        ok = await ctx.author.send(
            embed=discord.Embed(title="checking api",
                                description="Connecting to the api...",
                                color=0x5ca3ff))

        def lol():
            r = scraper.get(
                "https://rest-bf.blox.land/games/crash").json()["history"]
            yield [
                r[0]["crashPoint"],
                [float(crashpoint["crashPoint"]) for crashpoint in r[-2:]]
            ]

        for game in lol():
            games = game[1]
            avg = sum(games) / len(games)
            chance = 1
            for game in games:
                chance = chance = 95 / game
                prediction = (1 / (1 - (chance)) + avg) / 2
                if float(prediction) > 2:
                    color = 0x81fe8f
                else:
                    color = 0xfe8181
                desc = f"""
        **Crashpoint:**
        *{prediction:.2f}x*
        **Chance:**
              {chance:.2f}%
                      """
                em = discord.Embed(description=desc, color=color)
                await ok.edit(embed=em)

bot.run('discord bot token here)
# -- if ur using replit use this bellow and remove the bot.run above
# -- my_secret = os.environ['token']
# -- bot.run(my_secret)
