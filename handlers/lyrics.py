# Module by https://github.com/tofikdn
# Copyright (C) 2021 TdMusic

import requests
from pyrogram import Client
from config import BOT_USERNAME
from helpers.filters import command


@Client.on_message(command(["lirik", f"lirik@{BOT_USERNAME}"]))
async def lirik(_, message):
    try:
        if len(message.command) < 2:
            await message.reply_text("**Berikan Saya Judul Lagu !**")
            return
        query = message.text.split(None, 1)[1]
        rep = await message.reply_text("🔎 **Mencari Lirik Lagu...**")
        resp = requests.get(f"https://tede-api.herokuapp.com/api/lirik?l={query}").json()
        result = f"{resp['data']}"
        await rep.edit(result)
    except Exception:
        await rep.edit("**Lirik Tidak Ditemukan , Cari yang Bener Anjg!.** Jangan Spam Biar Ga Delay !")
