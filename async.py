import discord
from discord.ext import commands

import json
import asyncio
from PIL import Image, ImageDraw, ImageFont
from dispander import dispand
import os

import rw
import tea




global team_li
team_li = {
    "reset":"チームをリセットします",
    "make":"チームを新規作成します",
    "join":"既存のチームに所属します",
    "leave":"チームから脱退します",
    "del":"チームを削除します",
    "color":"チームカラーを変更します",
    "list":"チーム一覧を表示します"
}

# class Role(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#
#     @commands.command()
#     async def create(self, ctx, name):
#
#         guild = ctx.author.guild
#         role = discord.utils.get(guild.roles, name = name)
#
#         if role is None:
#             await guild.create_role(name = name)
#             await ctx.send(f"{name} を作成しました")
#         else:
#             await ctx.send(f"{name} は存在しています")
#
#     @commands.command()
#     async def delete(self, ctx, name):
#
#         guild = ctx.author.guild
#         role = discord.utils.get(guild.roles, name = name)
#
#         if role is None:
#             await ctx.send(f"{name} は存在していません")
#         else:
#             await role.delete()
#             await ctx.send(f"{name} を削除しました")
#
#     @commands.command()
#     async def add(self, ctx, name):
#
#         guild = ctx.author.guild
#         role = discord.utils.get(guild.roles, name = name)
#
#         if role is None:
#             await ctx.send(f"{name} は存在していません")
#         elif role in ctx.author.roles:
#             await ctx.send(f"{name} を所有しています")
#         else:
#             await ctx.author.add_roles(role)
#             await ctx.send(f"{name} を付与しました")
#
#     @commands.command()
#     async def remove(self, ctx, name):
#
#         guild = ctx.author.guild
#         role = discord.utils.get(guild.roles, name = name)
#
#         if role is None:
#             await ctx.send(f"{name} は存在していません")
#         elif role not in ctx.author.roles:
#             await ctx.send(f"{name} を所有していません")
#         else:
#             await ctx.author.remove_roles(role)
#             await ctx.send(f"{name} を剥奪しました")
#
# def setup(bot):
#     bot.add_cog(Role(bot))



class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):

        team = await rw.read(self)

        # print(team)

        await rw.write(team)

        print('Test is Ready!')

    @commands.Cog.listener()
    async def on_message(self, message):
        await dispand(message)
        pass

    @commands.command()
    async def team(self,ctx,*com):
        gui = str(ctx.author.guild.id)
        aut = str(ctx.author.id)
        com = list(com)
        team = await rw.read(self)

        # print(team)

        await rw.write(team)



        if com:
            if com[0] not in team_li:
                await ctx.send(f"{com[0]}は存在しません")
                return
            else:
                # if len(com) >= 2:
                #     if com[1] == "help":
                #         await ctx.send(f"{com[0]}の詳細：\n{team_li[com[0]]}")
                #         pass

                if com[0] == "reset":
                    await tea.reset(self,ctx,com,team)

                elif com[0] == "make":
                    await tea.make(self,ctx,com,team)

                elif com[0] == "join":
                    await tea.join(self,ctx,com,team)

                elif com[0] == "leave":
                    await tea.leave(self,ctx,com,team)

                elif com[0] == "del":
                    await tea.dele(self,ctx,com,team)

                elif com[0] == "color":
                    await tea.color(self,ctx,com,team)

                elif com[0] == "list":
                    await tea.lis(self,ctx,com,team)


                else:
                    await ctx.send("深刻なエラーが発生しました")


        else:
            await ctx.send("オプションを指定してください。")


    @commands.command()
    async def test(self,ctx,*com):
        com = list(com)
        if com:
            if com[0] not in com_li:
                await ctx.send(f"{com[0]}は存在しません")
                return
            else:
                if len(com) == 2:
                    await ctx.send(com_li[com[0]][com[1]])
                else:
                    await ctx.send("オプション指定がされていません。")
        else:
            await ctx.send("test")

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
    async def my(self,ctx):
        role = ctx.author.roles
        roles = role[1:]
        txt = ""
        for r in roles:
            txt += f"**{r}**\n"
        await ctx.send(f"__{ctx.author.display_name}__ の所属チーム：\n{txt}")

    # @commands.command()
    # async def make(self,ctx):
    #     guild = ctx.author.guild
    #     await guild.create_role(name="実験")

    @commands.command(pass_context=True)
    async def dele(self,ctx):
        guild = ctx.author.guild
        role = discord.utils.get(guild.roles, name="実験")
        if role:
            try:
              await role.delete()
              await ctx.send("The role {} has been deleted!".format(role.name))
            except discord.Forbidden:
              await ctx.send("Missing Permissions to delete this role!")
        else:
            await ctx.send("The role doesn't exist!")

    @commands.command()
    async def co(self,ctx):
        guild = ctx.author.guild
        arole = guild.roles
        role = discord.utils.get(guild.roles, name="実験")
        abc = len(arole)
        await role.edit(colour=discord.Colour.from_rgb(0, 100, 0),position=abc)



def setup(bot):
    bot.add_cog(Main(bot))
