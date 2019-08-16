from bot import bot
import event


@event.command()
async def unload(message, content):
    c = content.split()
    bot.unload_plugin(c[0])


@event.command()
async def load(message, content):
    c = content.split()
    bot.load_plugin(c[0])


@event.command()
async def reload(message, content):
    c = content.split()
    bot.reload_plugin(c[0])
