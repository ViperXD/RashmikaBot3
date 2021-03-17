from bs4 import BeautifulSoup
import urllib
from RashmikaBot import tbot
import glob
import io
import os
import re
import aiohttp
import urllib.request
from urllib.parse import urlencode

import bs4
import html2text
import requests
from bing_image_downloader import downloader
from googleapiclient.discovery import build
from PIL import Image
from telethon import *
from telethon.tl import functions
from telethon.tl import types
from telethon.tl.types import *

from RashmikaBot import *

from RashmikaBot.events import register

async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (
                await tbot(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerUser):
        return True


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res["items"]


@register(pattern="^/google (.*)")
async def _(event):
    if event.fwd_from:
        return
    approved_userss = approved_users.find({})
    for ch in approved_userss:
        iid = ch["id"]
        userss = ch["user"]
    if event.is_group:
        if await is_register_admin(event.input_chat, event.message.sender_id):
            pass
        elif event.chat_id == iid and event.sender_id == userss:
            pass
        else:
            return
    input_str = event.pattern_match.group(1)

    my_api_key = GOOGLE_SRCH_VALUE
    my_cse_id = GOOGLE_SRCH_KEY

    results = google_search(input_str, my_api_key, my_cse_id, num=10)

    output_str = " "
    for result in results:
        text = str(result["title"])
        url = str(result["link"])
        description = str(result["htmlSnippet"])
        last = html2text.html2text(description)
        output_str += "[{}]({})\n{}\n".format(text, url, last)

    await event.reply(
        "{}".format(output_str), link_preview=False, parse_mode="Markdown"
    )
