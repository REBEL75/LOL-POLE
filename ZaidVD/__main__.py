# ===========
# Zaid Is Running
# ===========

import asyncio
from pyrogram import Client, idle
from config import Zaid 
from ZaidVD.videoplayer import app
from ZaidVD.videoplayer import call_py

ZaidVD = Client(
    ":memory:",
    Zaid.API_ID,
    Zaid.API_HASH,
    bot_token=Zaid.BOT_TOKEN,
    plugins=dict(root="ZaidVD"),
)

ZaidVD.start()
print("[STATUS]:✅ »» BOT CLIENT STARTED ««")
app.start()
print("[STATUS]:✅ »» USERBOT CLIENT STARTED ««")
ZaidVD.start()
print("[STATUS]:✅ »» PYTGCALLS CLIENT STARTED ««")
idle()
print("[STATUS]:❌ »» BOT STOPPED ««")
