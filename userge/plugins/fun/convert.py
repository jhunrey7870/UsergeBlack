""" convert text """

# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.

from userge import userge, Message


@userge.on_cmd("small", about={
    'header': "Make caps smaller",
    'usage': "{tr}small [text | reply to msg]"})
async def small_(message: Message):
    """ text to small """
    text = message.input_str
    if message.reply_to_message:
        text = message.reply_to_message.text
    if not text:
        await message.err("input not found")
        return
    await message.edit(text.translate(str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                    "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘqʀꜱᴛᴜᴠᴡxʏᴢ")))


@userge.on_cmd("sfont", about={
    'header': "Convert text to struck",
    'usage': "{tr}sfont [text | reply to msg]"})
async def small_(message: Message):
    """ text to small """
    text = message.input_str
    if message.reply_to_message:
        text = message.reply_to_message.text
    if not text:
        await message.err("input not found")
        return
    await message.edit(text.translate(str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                    "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ")))


@userge.on_cmd("bscriptfont", about={
    'header': "Convert text to BoldScriptFont",
    'usage': "{tr}bscriptfont [text | reply to msg]"})
async def small_(message: Message):
    """ text to small """
    text = message.input_str
    if message.reply_to_message:
        text = message.reply_to_message.text
    if not text:
        await message.err("input not found")
        return
    await message.edit(text.translate(str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                    "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩")))


@userge.on_cmd("lower", about={
    'header': "Convert text to lowwer",
    'usage': "{tr}lower [text | reply to msg]"})
async def lower_(message: Message):
    """ text to lower """
    text = message.input_str
    if message.reply_to_message:
        text = message.reply_to_message.text
    if not text:
        await message.err("input not found")
        return
    await message.edit(text.lower())


@userge.on_cmd("upper", about={
    'header': "Convert text to upper",
    'usage': "{tr}upper [text | reply to msg]"})
async def upper_(message: Message):
    """ text to upper """
    text = message.input_str
    if message.reply_to_message:
        text = message.reply_to_message.text
    if not text:
        await message.err("input not found")
        return
    await message.edit(text.upper())
