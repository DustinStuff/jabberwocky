import event
import discord
from bot import bot
import time
# @event.message
# async def on_message(message: discord.Message):
#     print("{}: {}".format(message.author.display_name, message.content))


@event.message
async def on_message(message: discord.Message):
    if bot.config["print_output"]:
        t = time.strftime("%Y-%m-%d-%H:%M:%S", time.gmtime())
        server = message.guild.name
        channel = message.channel.name
        user = message.author.name
        print("{}#{}/{}/{}/ {}".format(server, channel, t, user, message.content))
