import aiohttp
from aiotg import Bot, Chat

import constants


bot = Bot(api_token=constants.api_token)

@bot.command("test1")
async def test1(chat: Chat, match):
    await chat.send_text("hello, test1")

bot.run()
