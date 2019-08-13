import json
import os

class Config(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = os.path.abspath("config.json")
        self.load_config()

    def reload_config(self):
        pass

    def load_config(self):
        with open(self.path) as f:
            self.update(json.load(f))
            #print(self.keys())