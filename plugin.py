import importlib
import os

class PluginManager:
    def __init__(self, plugins_dir="plugins"):
        self.plugin_directory = plugins_dir
        self.path = os.path.abspath(plugins_dir)
        self.plugins = {}
        #self.load_plugins()

    def load_plugins(self):
        plugin_names = [file[:-3] for file in os.listdir(self.path) if file[-3:] == ".py"]
        for plugin in plugin_names:
            self.load(plugin)

    def load(self, plugin_name):
        self.plugins[plugin_name] = importlib.import_module(self.plugin_directory + "." + plugin_name)

    def reload(self, plugin_name):
        importlib.reload(self.plugins[plugin_name])

    def reload_all(self):
        for plugin in self.plugins.values():
            importlib.reload(plugin)

    def unload(self, plugin_name):
        self.plugins.pop(plugin_name)
