from pyrogram import Client, filters
from pyrogram.types import Message

import tgcalls
import sira
from helpers.filters import sudoers
from helpers.wrappers import errors


@Client.on_message(
    filters.command("pause")
    & filters.group
    & ~ filters.edited
    & sudoers
)
@errors
async def pause(client: Client, message: Message):
    tgcalls.pytgcalls.pause_stream(message.chat.id)


@Client.on_message(
    filters.command("resume")
    & filters.group
    & ~ filters.edited
    & sudoers
)
@errors
async def resume(client: Client, message: Message):
    tgcalls.pytgcalls.resume_stream(message.chat.id)


@Client.on_message(
    filters.command(
        [
            "setvol", "set_vol", "vol", "setvolume", "set_volume", "volume"
        ]
    )
    & filters.group
    & ~ filters.edited
    & sudoers
)
@errors
async def volume(client: Client, message: Message):
    if len(message.command != 2):
        return

    try:
        volume = int(message.command[1])
    except:
        return

    if volume <= 0 and volume >= 200:
        tgcalls.pytgcalls.change_volume_call(message.chat.id, volume)
    else:
        return


@Client.on_message(
    filters.command(["clear", "clearqueue", "clear_queue"])
    & filters.group
    & ~ filters.edited
    & sudoers
)
@errors
async def clear(client: Client, message: Message):
    sira.clear(message.chat.id)


@Client.on_message(
    filters.command(["stop", "end"])
    & filters.group
    & ~ filters.edited
    & sudoers
)
@errors
async def stop(client: Client, message: Message):
    try:
        sira.clear(message.chat.id)
    except:
        pass

    tgcalls.pytgcalls.leave_group_call(message.chat.id)
