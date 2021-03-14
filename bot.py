import discord
from discord.ext import commands
from discord_slash import SlashCommand

from os import environ


class Zect(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or(environ.get('PREFIX', '/')),
            help_command=None,
        )
        self.slash = SlashCommand(self, sync_commands=True)
    async def on_ready(self):
        print("I am ready")
