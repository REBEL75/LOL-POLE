#ur Motherfucker If U Kang And Don't Give Creadits ๐ฅด ๐ญ๐๐ผ๐๐ฟ

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
    m = await message.reply_text("๐ **ีแดแฉแแแผIแแ แแแช...**")
    try:
        if len(message.command) < 2:
            await message.reply_text("`/search` needs an argument!")
            return
        query = message.text.split(None, 1)[1]
        results = YoutubeSearch(query, max_results=5).to_dict()
        i = 0
        text = ""
        while i < 5:
            text += f"**๐๐๐ฆ๐:** `{results[i]['title']}`\n"
            text += f"**๐๐ฎ๐ซ๐๐ญ๐ข๐จ๐ง:** {results[i]['duration']}\n"
            text += f"**๐๐ข๐๐ฐ๐ฌ:** {results[i]['views']}\n"
            text += f"**๐๐ก๐๐ง๐ง๐๐ฅ:** {results[i]['channel']}\n"
            text += f"https://www.youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await m.edit(str(e))
