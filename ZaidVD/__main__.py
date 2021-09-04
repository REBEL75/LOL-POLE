from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from ZaidVD.videoplayer import app


ZaidVD = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="ZaidVD"),
)

ZaidVD.start()
print("[INFO]: STARTING BOT CLIENT")
app.start()
print("[INFO]: STARTING USERBOT CLIENT")
idle()
