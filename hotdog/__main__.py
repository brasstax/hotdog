#!/usr/bin/env python3.8
# __main__.py

import sys
import os
from os.path import expanduser
import importlib.resources
from configparser import ConfigParser
import discord
from discord.ext import commands
import logging


logging.basicConfig(level=logging.INFO)
INI_FILE = os.environ.get("HOTDOG_TOKEN_FILE", f"{expanduser('~')}/hotdog.cfg")
config = ConfigParser()
try:
    os.stat(INI_FILE)
except FileNotFoundError as e:
    with importlib.resources.path("hotdog", "token.sample.cfg") as p:
        package_path = p
    msg = "No HOTDOG_TOKEN_FILE env configured. "
    msg += f"Copy {package_path} to {expanduser('~')}/hotdog.cfg and add your discord bot token."
    sys.exit(msg)
config.read(INI_FILE)
try:
    token = config["general"]["token"]
except ValueError:
    sys.exit(f"No 'token' value found under 'general' section in {INI_FILE}.")
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    description="!hotdog",
    case_insensitive=True,
)

class Commands(commands.Cog, name="Hotdog"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hotdog", aliases=["hatdog"])
    async def hotdog(self, ctx):
        """
        Hotdog.
        """
        guild = ctx.guild if ctx.guild else "a direct message"
        logging.info(f"hotdog requested by {ctx.author} in {guild}.")
        message = ctx.message
        return await message.add_reaction("🌭")

bot.add_cog(Commands(bot))

@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user}.")
    activity = discord.Game(name="!hotdog")
    await bot.change_presence(status=discord.Status.online, activity=activity)


def main():
    bot.run(token)

if __name__ == '__main__':
    main()
