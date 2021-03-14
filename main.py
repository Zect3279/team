from os import environ

from bot import Zect


bot = Zect()

extensions = [
    "async"
]
for extension in extensions:
    bot.load_extension(extension)

bot.run(environ["BOT_TOKEN"])
