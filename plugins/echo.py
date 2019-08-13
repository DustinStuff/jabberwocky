import event
import discord

# @event.message
# async def on_message(message: discord.Message):
#     print("{}: {}".format(message.author.display_name, message.content))


@event.message
async def on_message(message: discord.Message):
    if message.channel.name == "bottest_":
        if message.author.display_name == "Dustin":
            await message.channel.send("Hi")
        return