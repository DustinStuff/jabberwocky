import discord.ext.commands
import config, event, plugin


class Bot(discord.ext.commands.Bot):
    def __init__(self, command_prefix="@"):
        super().__init__(command_prefix=command_prefix)
        self.counter = 1
        self.config = config.Config()
        self.plugin_manager = plugin.PluginManager()

    def run_(self):
        super().run(self.config["key"])

    def load_config(self):
        self.config.load_config()

    async def on_ready(self):
        print("READY")

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content[0] == self.command_prefix:
            await event.emit_command(message)
        await event.emit_message(message)
        await self.process_commands(message)


bot = Bot()
bot.plugin_manager.load_plugins()
