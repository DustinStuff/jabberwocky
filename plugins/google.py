import event
import requests
import discord
from bot import bot

@event.command(alias=["g", "google"])
async def google(message, content):
    API_URL = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": bot.config["api_keys"]["google"],
        "q": content,
        "cx": "004603819845543257192:vn_rcth-y1c",  # TODO: move this to a config file.
        "safe": "active"
    }

    r = requests.get(API_URL, params=params)
    if r.status_code != 200:
        print(r.status_code)
        return "Error"

    js = r.json()
    result_0 = js["items"][0]
    title = result_0["title"]
    link = result_0["link"]
    snip = result_0["snippet"]

    embed = discord.Embed(title=title, url=link, description=snip, color=discord.Color.teal())
    await message.channel.send(embed=embed)
