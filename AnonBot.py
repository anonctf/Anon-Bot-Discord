import os
import random
import re
import requests
import discord
from discord.ext import commands
from keep_alive import keep_alive
from HelperFunctions import HELP
from HelperFunctions import quotes

# bot icon url
bot_icon = "https://avatars1.githubusercontent.com/u/68417148?s=460&u=435dc029d21620348712b79f581121e6be4950ad&v=4"

def main(bot):
    # Confirms successful bot login
    @bot.event
    async def on_ready():
        await bot.change_presence(activity=discord.Game('Cyberpunk'))
        print('Logged in as {0.user}'.format(bot))


    # Bot commands

    ########
    # Help #
    ########
    @bot.command(name='help')
    async def help(ctx, arg=""):
        if arg == "":
            e = HELP()
        else:
            e = HELP(arg)
        await ctx.channel.send(embed=e)

    ###############
    # Greet hello #
    ###############
    @bot.command(name='hello')
    async def hello(ctx):
        await ctx.author.send(f"Hello, {ctx.author.name}!")

    #####################
    # Random bot quotes #
    #####################
    @bot.command(name='ab')
    async def ab(ctx):
        bot_quotes = quotes['anonbot']
        quote = bot_quotes[random.randint(0, len(bot_quotes) - 1)]
        response = discord.Embed(title=quote, color=0xbf0f0f)
        response.set_author(name="Anon-Bot", icon_url="https://youthful-minsky-60409b.netlify.app/images/anonymous.png")
        await ctx.channel.send(embed=response)

    ##############
    # xkcd comic #
    ##############
    @bot.command(name='xkcd')
    async def xkcd_api(ctx):
        comic_number = random.randint(1, 2406)
        url = f"https://xkcd.com/{comic_number}/info.0.json"
        res = requests.get(url).json()

        e = discord.Embed(title=res["safe_title"], description=res["alt"], color=0x58a8d6)
        e.set_image(url=res["img"])
        e.set_author(name="Anon Bot", icon_url=bot_icon)
        e.set_footer(text="Random comic from xkcd API!!")
        await ctx.channel.send(embed=e)

    ################
    # number facts #
    ################
    @bot.command(name='numfact')
    async def fact(ctx, arg1="", arg2=""):
        if arg1 == "":
            url = "http://numbersapi.com/random"
        elif arg1 == "date":
            u_in = re.match(r"\d{1,2}/\d{1,2}", arg2)
            if u_in:
                d = u_in[0]
            else:
                await ctx.channel.send("Invalid arg2, sending my choice")
                month = random.randint(1,12)
                day = random.randint(1,31)
                d = str(month) + '/' + str(day) 
            url = f"http://numbersapi.com/{d}/date"
        elif arg1 == "year":
            u_in = re.match(r"\d{1,4}", arg2)
            if u_in and int(u_in[0]) <= 2020:
                y = u_in[0]
            else:
                await ctx.channel.send("Invalid arg2, sending my choice")
                y = "random"
            url = f"http://numbersapi.com/{y}/year"
        elif arg1 == "math":
            u_in = re.match(r"\d+", arg2)
            if u_in:
                m = u_in[0]
            else:
                await ctx.channel.send("Invalid arg2, sending my choice")
                m = "random"
            url = f"http://numbersapi.com/{m}/math"
        else:
            e = HELP("numfact")
            await ctx.channel.send(embed=e)
            return
    
        r = requests.get(url).text

        e = discord.Embed(title="Number Fact", description=r, color=0x48b8d9)
        e.set_author(name="Anon Bot", icon_url=bot_icon)
        await ctx.channel.send(embed=e)

if __name__ == "__main__":
    # Command Prefix
    bot = commands.Bot(command_prefix="!", help_command=None)

    main(bot)
    keep_alive()

    # Starts the bot
    bot.run(os.getenv("TOKEN"))
