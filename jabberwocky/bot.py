import discord
import json
import config


class Bot:
    def __init__(self):
        self.counter = 1
        self.client = discord.Client()
        self.config = config.Config()
        print(self.config["key"])
        # self.client.run(self.config["key"])
    def run(self):
        self.client.run(self.config["key"])


bot = Bot()


@bot.client.event
async def on_message(message):
    if message.author == bot.client.user:
        return
    print(message.content)
    if message.content.startswith('!yee'):
        await message.channel.send('<:yee:442367221381988362>')
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')


@bot.client.event
async def on_ready():
    print("ready")
