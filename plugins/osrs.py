import event
import requests
import discord


class WikiSearch:
    # See: https://oldschool.runescape.wiki/w/mw:API:Main_page for more info.
    API_URL = "https://oldschool.runescape.wiki/api.php"

    def __init__(self, search_term):
        self.search_term = search_term
        self.url = ""
        self.title = ""
        self.description = ""
        self.search()

    def search(self):
        params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": self.search_term,
            "srnamespace": "0|4",
            "srprop": "sectionsnippet|sectiontitle"
        }
        r = requests.get(WikiSearch.API_URL, params=params)
        print(r.status_code)
        json = r.json()

        self.get_info(json["query"]["search"][0]["title"])

    def get_info(self, title):
        params = {
            "action": "query",
            "format": "json",
            "prop": "extracts|info",
            "titles": title,
            "exchars": "300",
            "exintro": 1,
            "explaintext": 1,
            "inprop": "url|displaytitle"
        }
        r = requests.get(WikiSearch.API_URL, params=params)
        json = r.json()
        l = json["query"]["pages"]
        l = list(l.values())[0]
        if l["pageid"] != "-1":
            self.url = l["fullurl"]
            self.title = l["title"]
            self.description = l["extract"]


@event.command()
async def osrs(message, content):
    result = WikiSearch(content)
    url = result.url
    description = result.description
    title = result.title
    color = discord.Colour.teal()

    embed = discord.Embed(title=url, url=url, color=color)
    embed.add_field(name=title, value=description)
    await message.channel.send(embed=embed)
