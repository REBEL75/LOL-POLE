#ur Motherfucker If U Kang And Don't Give Creadits 🥴 𝙭𝙕𝘼𝙄𝘿

import logging

from pyrogram import Client as app
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from config import Zaid
from helpers.filters import command

# logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@app.on_message(command(["search", f"search@{Zaid.BOT_USERNAME}"]))
async def ytsearch(_, message: Message):
    m = await message.reply_text("🔎 **ՏᗴᗩᖇᑕᕼIᑎᘜ ᑌᖇᒪ...**")
    try:
        if len(message.command) < 2:
            await message.reply_text("`/search` needs an argument!")
            return
        query = message.text.split(None, 1)[1]
        results = YoutubeSearch(query, max_results=5).to_dict()
        i = 0
        text = ""
        while i < 5:
            text += f"**𝐍𝐚𝐦𝐞:** `{results[i]['title']}`\n"
            text += f"**𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧:** {results[i]['duration']}\n"
            text += f"**𝐕𝐢𝐞𝐰𝐬:** {results[i]['views']}\n"
            text += f"**𝐂𝐡𝐚𝐧𝐧𝐞𝐥:** {results[i]['channel']}\n"
            text += f"https://www.youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await m.edit(str(e))
