import discord
from discord.ext import commands

import json
import asyncio
from PIL import Image, ImageDraw, ImageFont
from dispander import dispand
import os

from lib.rw import RW



class Move(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.rw = RW(bot)


    def ga(self,ctx):
        return str(ctx.author.guild.id),str(ctx.author.id)

    async def reset(self,ctx,com,team):
        gui,aut = ga(ctx)
        if ctx.author == self.bot.get_user(653785595075887104):
            team = {}
            await self.rw.write(team)
            await ctx.send("チームをリセットしました")
            print("チームがリセットされました")

    async def make(self,ctx,com,team):
        gui,aut = ga(ctx)
        if not com[1]:
            await ctx.send("チーム名が指定されていません")
        else:
            if com[1] in team[gui]["list"]:
                await ctx.send(f"{com[1]}は存在します")
                return
            else:
                team[gui]["list"].append(com[1])
                await self.rw.write(team)

                guild = ctx.author.guild
                await guild.create_role(name=com[1])

                await ctx.send(f"チーム**{com[1]}**が作成されました")
                print(f"チーム{com[1]}が作成されました")

    async def join(self,ctx,com,team):
        gui,aut = ga(ctx)
        if not com[1]:
            await ctx.send("チーム名が指定されていません")

        elif com[1] not in team[gui]["list"]:
            await ctx.send(f"チーム**{com[1]}**は存在しません")


        else:
            try:
                team[gui][aut].append(com[1])

            except KeyError as e:
                team[gui][aut] = com[1]

            finally:
                try:
                    guild = ctx.author.guild
                    role = discord.utils.get(guild.roles, name=com[1])
                    member = ctx.author
                    await member.add_roles(role)

                    await ctx.send(f"チーム**{com[1]}**に所属しました")
                    print(f"{ctx.author.display_name}がチーム{com[1]}に所属しました")
                    await self.rw.write(team)

                except discord.Forbidden:
                    await ctx.send("権限レベルが足りません")

    async def leave(self,ctx,com,team):
        gui,aut = ga(ctx)
        if not com[1]:
            await ctx.send("チーム名が指定されていません")

        elif com[1] not in team[gui]["list"]:
            await ctx.send(f"チーム**{com[1]}**は存在しません")

        elif aut not in team[gui]:
            await ctx.send("チームに所属していません。")

        else:
            at = com[1]
            team[gui][aut].remove(at)


            guild = ctx.author.guild
            role = discord.utils.get(guild.roles, name=at)
            member = ctx.author
            await member.remove_roles(role)


            await ctx.send(f"チーム**{at}**から脱退しました")
            print(f"{ctx.author.display_name}がチーム{at}から脱退しました")
            await self.rw.write(team)



    async def dele(self,ctx,com,team):
        gui,aut = ga(ctx)
        role = ctx.author.roles
        lal = []
        for l in role:
            lal.append(l.name)
        if ("Owner" or "Admin" or "管理者" or "副管理者") not in lal:
            await ctx.send("権限レベルが足りません")

        elif not com[1]:
            await ctx.send("チーム名が指定されていません")

        elif com[1] not in team[gui]["list"]:
            await ctx.send(f"チーム**{com[1]}**は存在しません")

        else:
            lit = team[gui]["list"]
            lit.remove(com[1])
            guild = ctx.author.guild
            role = discord.utils.get(guild.roles, name=com[1])
            await role.delete()
            await ctx.send(f"チーム**{com[1]}**を削除しました")
            print(f"チーム{com[1]}を削除しました")
            await self.rw.write(team)

    async def color(self,ctx,com,team):
        gui,aut = ga(ctx)
        if not com[1]:
            await ctx.send("チーム名が指定されていません")

        elif com[1] not in team[gui]["list"]:
            await ctx.send(f"チーム**{com[1]}**は存在しません")

        else:
            if len(com) == 5:
                guild = ctx.author.guild
                role = discord.utils.get(guild.roles, name=com[1])
                r = int(com[2])
                g = int(com[3])
                b = int(com[4])
                im = Image.new("RGB", (50, 50), (r,g,b))
                # im
                im.save('pic.png')
                await role.edit(colour=discord.Colour.from_rgb(r,g,b))
                await ctx.send(f"チーム**{com[1]}**の色が__rgb({r},{g},{b})__に変更されました", file=discord.File('pic.png'))
                # await ctx.send()
                print(f"チーム{com[1]}の色がrgb({r},{g},{b})に変更されました")
                os.remove('pic.png')
            else:
                await ctx.send("色のR,G,Bを指定してください")

    async def lis(self,ctx,com,team):
        gui,aut = ga(ctx)
        if len(com) == 2:
            if com[1] == "me":
                role = ctx.author.roles
                roles = role[1:]
                txt = ""
                for r in roles:
                    txt += f"**{r}**\n"
                await ctx.send(f"__{ctx.author.display_name}__ の所属チーム：\n{txt}")
        else:
            txt = "このサーバー内のチーム一覧\n```"
            for name in team[gui]["list"]:
                txt += f"\n{name}"
            await ctx.send(f"{txt}\n```")

    async def in(self,ctx,com,team):
        role = ctx.author.roles
        roles = role[1:]
        txt = ""
        for r in roles:
            txt += f"**{r}**\n"
        await ctx.send(f"__{ctx.author.display_name}__ の所属チーム：\n{txt}")
