import discord
import enum
from functools import wraps

_handlers = {"command": [], "message": []}


class Event:
    def __init__(self, module: str, handler):
        self.module = module
        self._handler = handler

    async def execute(self, *args, **kwargs):
        await self._handler(*args, **kwargs)


class MessageEvent(Event):
    pass


class CommandEvent(Event):
    def __init__(self, module, handler, aliases=[]):
        super().__init__(module, handler)
        self.aliases = aliases

    async def execute(self, *args, **kwargs):
        msg = kwargs["message"]
        content = msg.content.split()[1:]
        kwargs_ = {"message": msg, "content": content}
        await self._handler(*args, **kwargs_)


def _add_handler(handler: Event, type_):
    _handlers[type_].append(handler)
    """
    _handlers = {
    "commands": [CommandEvent, CommandEvent_2, etc]
    """


def message(func):
    @wraps(func)
    async def wrapper(msg):
        f = await func(msg)
        if type(f) is str:
            await msg.channel.send(f)
    _add_handler(MessageEvent(func.__module__, wrapper), "message")
    return wrapper


async def emit_message(msg):
    for f in _handlers["message"]:
        await f.execute(msg)


def command(alias=[]):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            msg = kwargs["message"]
            content = kwargs["content"]
            f = await func(*args, **kwargs)
            if type(f) is str:
                await msg.channel.send(f)

        cmd = CommandEvent(func.__module__, wrapper, alias)
        if len(alias) > 0:
            cmd.aliases = alias
        else:
            cmd.aliases = [func.__name__]

        _add_handler(cmd, "command")
        return wrapper

    return decorator


async def emit_command(msg):
    content = msg.content.split()
    command_word = content[0][1:]

    for c in _handlers["command"]:
        if command_word in c.aliases:
            await c.execute(message=msg, content=content)

