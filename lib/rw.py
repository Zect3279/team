import discord
from discord.ext import commands

import json
import asyncio

class RW(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    async def read(self):
        with open("json/team.json", mode="r", encoding='utf-8') as f:
            team = json.load(f)
            f.close()
        for guild in self.bot.guilds:
            roles = guild.roles
            role = roles[1:]
            txt = []
            for r in role:
                txt.append(r.name)
            try:
                team[str(guild.id)]["list"] = txt
            except KeyError as e:
                print(e)
                team[str(guild.id)] = {"list" : txt}
            finally:
                for member in guild.members:
                    role = member.roles
                    del role[0]
                    lal = []
                    if role:
                        for l in role:
                            lal.append(l.name)
                        team[str(guild.id)][str(member.id)] = lal
                    else:
                        pass
        return team



        # role = ctx.author.roles
        # roles = role[1:]
        # txt = ""
        # for r in roles:
        #     txt += f"**{r}**\n"
        # await ctx.send(f"__{ctx.author.display_name}__ の所属チーム：\n{txt}")



    async def write(self,team):
        with open("json/team.json", mode="w", encoding='utf-8') as f:
            WriteTeam = json.dumps(team, ensure_ascii=False, indent=2)
            f.write(WriteTeam)
            f.close()
        return team
