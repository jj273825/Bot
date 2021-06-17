import discord

From discord.ext import commands

bot = commands.Bot(command_prefix="?")

@bot.event
async def on_ready():
    print(">> 洨瑋上線 <<")

bot.run("ODU0OTE4MTM5NTk0ODAxMTgz.YMq6kA.YGHJwCLQFyOFnVTwmQPoyiNLwt0")