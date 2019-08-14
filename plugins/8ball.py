import event
from random import choice

ball_file = "plugins/8ball.txt"


@event.command(alias=["8ball", "8"])
async def eightball(message, content):
    with open(ball_file) as f:
        answers = f.read().splitlines()
    return choice(answers)
