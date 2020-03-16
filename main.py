import aiohttp
import os
from aiotg import Chat

from bot import Bot
import constants


# bot = Bot(api_token=constants.api_token)

def get_moderators():
    moderators = [132982472, 316296712]  # nonamenix  # makedonski
    # try:
    #     moderators = os.environ["MODERATORS"]
    # except KeyError:
    #     pass
    # else:
    #     moderators = [int(m.strip()) for m in moderators.split(" ")]
    # logger.info("Moderators: %s", moderators)
    return moderators

bot = Bot(
    api_token=constants.api_token,
    # healthcheckio_token=os.environ["HEALTHCHECKIO_TOKEN"],
    moderators=get_moderators(),
    # mongo_url=os.environ.get("MONGO_URL"),
    # mongo_healthcheckio_token=os.environ.get("MONGO_HEALTHCHECKIO_TOKEN"),
)


communities = {'spbpython': 'SPb Python123', 
                '1': '11',
                '2': '22',
                '3': '33',
}

communities_low_names = [''.join(community.lower().split()) for community in communities]

months = {
    'январь': 'jan',
    'февраль': 'feb',
    'март': 'mar',
    'апрель': 'apr',
    'май': 'may',
    'июнь': 'jun',
    'июль': 'jul',
    'август': 'aug',
    'сентябрь': 'sep',
    'октябрь': 'oct',
    'ноябрь': 'nov',
    'декабрь': 'dec'
}

@bot.moderator_command("/?ping$")
async def ping(chat, message):
    await chat.reply("pong")

@bot.command("test1")
async def test1(chat: Chat, match):
    await chat.send_text("hello, test1")
    await chat.send_text(chat.sender["id"])

@bot.command("start")
async def start(chat: Chat, match):
    await chat.send_text("1: Сообщества\n2: Календарь")
    
@bot.command("Сообщества")
async def id(chat: Chat, match):
    await chat.send_text('\n'.join(communities))

@bot.command("Календарь")
async def id(chat: Chat, match):
    await chat.send_text('\n'.join(months))

@bot.command("/?(?P<key>.+)")
async def community_link(chat: Chat, matched):
    key = ''.join(matched.group("key").lower().split())
    print('key:', key)

    if key in communities_low_names:
        community_drinkup = [community_drinkup for keys, community_drinkup in communities.items()][0]
        await chat.send_text(community_drinkup)
    elif key in months:
        month_drinkups = [month_drinkups for keys, month_drinkups in months.items() if key in keys][0]
        await chat.send_text(month_drinkups)
    else:
        await chat.send_text('No info')

bot.run()
