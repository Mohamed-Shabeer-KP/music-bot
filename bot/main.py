import discord
from discord.ext import commands
import os

token = os.getenv("DISCORD_BOT_TOKEN")

description = '''An example bot to showcase the discord.ext.commands extension module.'''
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='.', description=description, intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def uyir(ctx, msg:str):
    await ctx.send('{0} ഉയിർ ആണ് ❤'.format(msg))

bot.run(token)