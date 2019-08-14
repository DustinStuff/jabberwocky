import event
from bot import bot
import requests
# TODO: This should all be changed to be way more flexible at some point.

@event.command()
async def update(message, content):
    print("yeet")
    c = content.split()
    plugins_dir = bot.config["plugins"]["plugins_remote_directory"]
    r = requests.get(plugins_dir)
    if r.status_code != 200:
        return "Error reading from remote plugin directory."
    js = r.json()
    for entry in js:
        if entry["name"] == c[0]:
            remote_plugin = requests.get(entry["download_url"])
            with open("plugins/{}".format(c[0]), "w") as f:
                f.write(remote_plugin.text)
            return "Success"