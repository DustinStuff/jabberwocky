import event
import xdice

@event.command(["roll"])
async def roll(message, content):
    dice = xdice.roll(content)
    return "{} = {}".format(dice.format(), dice)
