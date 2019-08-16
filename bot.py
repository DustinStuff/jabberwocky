import discord.ext.commands
import config, event, plugin
import logging
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger("jabberwocky")
logger.info("Started")


class Bot(discord.Client):
    def __init__(self):
        super().__init__()
        self.counter = 1
        self.config = config.Config()
        self.plugin_manager = plugin.PluginManager()

        self.command_prefix = self.config["command_prefix"]

    def run(self):
        super().run(self.config["key"])

    def load_config(self):
        self.config.load_config()

    def load_plugin(self, name):
        self.plugin_manager.load(name)

    def reload_plugin(self, name):
        event.remove_handler(name)
        self.plugin_manager.reload(name)

    def unload_plugin(self, name):
        event.remove_handler(name)
        #self.plugin_manager.unload(name)

    async def on_ready(self):
        logger.info("READY")

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content[0] == self.command_prefix:
            await event.emit_command(message)
        await event.emit_message(message)


bot = Bot()
bot.plugin_manager.load_plugins()
