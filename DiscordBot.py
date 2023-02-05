import asyncio
import discord
from discord.ext import commands

#import cog
from help_cog import help_cog

intents = discord.Intents.default()
intents.message_content = True
prefix = '$'
bot = commands.Bot(command_prefix=prefix, intents=intents)

async def setup(bot):
    await bot.add_cog(help_cog(bot, prefix))
    

token = ""
with open("token.txt") as f:
    token = f.read() 

asyncio.run(setup(bot))

bot.run(token)
