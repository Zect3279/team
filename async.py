import discord
from discord.ext import commands

import json
import asyncio
from PIL import Image, ImageDraw, ImageFont
from dispander import dispand
import os

from lib.rw import RW
from lib.tea import Move




class Team(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.move = Move(bot)
        self.rw = RW(bot)
        self.help_li = {
            "reset":"チームをリセットします",
            "make":"チームを新規作成します",
            "join":"既存のチームに所属します",
            "leave":"チームから脱退します",
            "del":"チームを削除します",
            "color":"チームカラーを変更します",
            "list":"チーム一覧を表示します",
            "in":"現在所属しているチームを表示"
        }


    @commands.Cog.listener()
    async def on_ready(self):
        team = await self.rw.read()
        # DEBUG: print(team)
        await self.rw.write(team)


    @commands.command()
    async def team(self,ctx,*com):
        if com == None:
            return

        gui = str(ctx.author.guild.id)
        aut = str(ctx.author.id)
        com = list(com)
        team = await self.rw.read()

        # DEBUG: print(team)

        await self.rw.write(team)

        if com:
            if com[0] not in self.help_li:
                await ctx.send(f"{com[0]}は存在しません")
                return
            else:
                # if len(com) >= 2:
                #     if com[1] == "help":
                #         await ctx.send(f"{com[0]}の詳細：\n{team_li[com[0]]}")
                #         pass

                if com[0] == "reset":
                    await self.move.reset(ctx,com,team)

                elif com[0] == "make":
                    await self.move.make(ctx,com,team)

                elif com[0] == "join":
                    await self.move.join(ctx,com,team)

                elif com[0] == "leave":
                    await self.move.leave(ctx,com,team)

                elif com[0] == "del":
                    await self.move.dele(ctx,com,team)

                elif com[0] == "color":
                    await self.move.color(ctx,com,team)

                elif com[0] == "list":
                    await self.move.lis(ctx,com,team)

                elif com[0] == "in":
                    await self.move.on(ctx,com,team)


                else:
                    await ctx.send("深刻なエラーが発生しました")


        else:
            await ctx.send("オプションを指定してください。")


    @commands.command()
    async def role(self,ctx):
        guild = ctx.author.guild
        roles = guild.roles
        role = roles[1:]
        txt = ""
        for r in role:
            txt += f"{r}\n"
        print(txt)
        await ctx.send(f"```\n{txt}```")

    @commands.command()
    async def rgb(self,ctx):
        await ctx.send("https://www.colordic.org/")

def setup(bot):
    bot.add_cog(Team(bot))
