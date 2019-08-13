import discord
from functools import wraps

_message_handlers = []
_ready_handlers = []
_command_handlers = []


def message(func):
    @wraps(func)
    async def wrapper(msg):
        f = await func(msg)
        if type(f) is str:
            await msg.channel.send(f)
    _message_handlers.append(wrapper)
    return wrapper


async def emit_message(msg):
    for f in _message_handlers:
        await f(msg)


def command(alias=[]):
    command_info = {"aliases": []}

    def decorator(func):
        if len(alias) == 0:
            command_info["aliases"].append(func.__name__)
        else:
            command_info["aliases"] = alias

        @wraps(func)
        async def wrapper(*args, **kwargs):
            msg = kwargs["message"]
            content = kwargs["content"]
            f = await func(*args, **kwargs)
            if type(f) is str:
                await msg.channel.send(f)

        command_info["handler"] = wrapper
        return wrapper

    _command_handlers.append(command_info)
    return decorator


async def emit_command(message):
    content = message.content.split()
    command_word = content[0][1:]

    for c in _command_handlers:
        if command_word in c["aliases"]:
            f = c["handler"]
            await f(message=message, content=content)

