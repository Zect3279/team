import discord
from discord.ext import commands

import json
import asyncio
from dispander import dispand
import rw



class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):

        team = await rw.read(self)

        print(team)

        await rw.write(team)

        print('Test is Ready!')

    @commands.Cog.listener()
    async def on_message(self, message):
        await dispand(message)
        pass

    @commands.command()
    async def team(self,ctx,*com):
        guild = ctx.author.guild
        roles = guild.roles
        role = roles[1:]
        txt = ""
        for r in role:
            txt += f"{r}\n"
        gui = str(ctx.author.guild.id)
        aut = str(ctx.author.id)
        com = list(com)
        team = await rw.read(self)

        # print(team)

        await rw.write(team)



def setup(bot):
    bot.add_cog(Main(bot))
