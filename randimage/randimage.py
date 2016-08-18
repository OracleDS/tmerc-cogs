import os
import random

import discord
from discord.ext import commands

class Randimage:
    """Picks a random image from the given directory."""

    def __init__(self, bot):
        self.bot = bot
        self.base = "data/randimage/"

    def _list_image_dirs(self):
        ret = []
        for thing in os.listdir(self.base):
            if os.path.isdir(os.path.join(self.base, thing)):
                ret.append(thing)
        return ret

    @commands.command(pass_context=True, no_pm=True, name="randimage")
    async def _randimage(self, context, dirname):
        """Chooses a random image from the given directory (inside \"data/randimage\") and sends it."""

        self.bot.type()
        lists = self._list_image_dirs()

        if not any(map(lambda l: os.path.split(l)[1] == dirname, lists)):
            await self.bot.reply("Image directory not found.")
            return

        direc = os.path.join(self.base, dirname)

        if not os.listdir(direc):
            await self.bot.reply("There are no images in that directory.")
            return

        await self.bot.upload(os.path.join(direc, random.choice(os.listdir(direc))))

def setup(bot):
    bot.add_cog(Randimage(bot))
