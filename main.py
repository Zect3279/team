from bot import Zect
import setting


bot = Zect()

BOT_TOKEN = setting.BOT

extensions = [
    "async"
]
for extension in extensions:
    bot.load_extension(extension)

bot.run(BOT_TOKEN)
