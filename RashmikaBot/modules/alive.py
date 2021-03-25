#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ALEN TL

from telethon import events, Button, custom
import re, os
from RashmikaBot.events import register
from RashmikaBot import telethn as tbot
from RashmikaBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/1ed503f954d7d1fa0477b.jpg"
@register(pattern=("/alive"))
async def awake(event):
  rashmika = event.sender.first_name
  RASHMIKA = "HELLO THIS IS RASHMIKA MANDANNA \n\n"
  RASHMIKA += "ALL SYSTEM WORKING PROPERLY\n\n"
  RASHMIKA += "RASHMIKA OS : 1.0 LATEST\n\n"  
  RASHMIKA += f"MY MASTER {rashmika} ☺️\n\n"
  RASHMIKA += "FULLY UPDATED\n\n"
  RASHMIKA += "TELETHON : 1.19.5 LATEST\n\n"
  RASHMIKA += "THANKS FOR ADDING ME HERE"
  BUTTON = [[Button.url("MASTER", "https://t.me/ALEN_TL"), Button.url("DEVLOPER", "https://t.me/ALEN_TL")]]
  BUTTON += [[custom.Button.inline("REPOSITORIES", data="RASHMIKA")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=RASHMIKA,  buttons=BUTTON)




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"RASHMIKA")))
async def callback_query_handler(event):
  ALEN = [[Button.url("REPO-RASHMIKA MANDANNA", "https://github.com/ALENTL/RashmikaBot3"), Button.url("REPO-AnyDLBot", "https://github.com/ALENTL/AnyDLBot")]]
  ALEN +=[[Button.url("DEPLOY-RASHMIKA MANDANNA", "https://heroku.com/deploy?template=https://github.com/ALENTL/RashmikaBot3"), Button.url("DEPLOY-AnyDLBot", "https://heroku.com/deploy?template=https://github.com/ALENTL/AnyDLBot")]]
  ALEN +=[[Button.url("STRING-SESSION", "https://repl.it/@ALEN2005/GenerateStringSession")]]
  ALEN +=[[Button.url("API_ID & HASH", "https://t.me/midukkanscraper_bot"), Button.url("REDIS", "https://redislabs.com")]]
  ALEN +=[[Button.url("SUPPORT CHANNEL", "https://t.me/focusgrpchannel"), Button.url("SUPPORT GROUP", "https://t.me/focusmoviess")]]
  ALEN +=[[custom.Button.inline("ALIVE", data="ATL")]]
  await event.edit(text=f"ALL DETAILS OF REPOS", buttons="ALEN")


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ATL")))
async def callback_query_handler(event):
  global PHOTO
  rashmika = event.sender.first_name
  RASHMIKA = "HELLO THIS IS RASHMIKA MANDANNA \n\n"
  RASHMIKA += "ALL SYSTEM WORKING PROPERLY\n\n"
  RASHMIKA += "RASHMIKA OS : 1.0 LATEST\n\n"
  RASHMIKA += f"MY MASTER {rashmika} ☺️\n\n"
  RASHMIKA += "FULLY UPDATED BOT\n\n"
  RASHMIKA += "TELETHON : 1.19.5 LATEST\n\n"
  RASHMIKA += "THANKS FOR ADDING ME HERE"
  BUTTONS = [[Button.url("MASTER", "https://t.me/ALEN_TL"), Button.url("DEVLOPER", "https://t.me/ALEN_TL")]]
  BUTTONS += [[custom.Button.inline("REPOSITORYS", data="RASHMIKA")]]
  await event.edit(text=RASHMIKA, buttons=BUTTONS)


@register(pattern=("/repo|/REPO"))
async def repo(event):
  await tbot.send_message(event.chat, "REPO OF RASHMIKA MANDANNA", buttons=[[Button.url("⚜️REPO⚜️", "https://github.com/ALENTL/RashmikaBot3")]])

__help__ = """
 - /alive check bot alive or die
 - /repo for this bot repo
"""
__mod_name__ = "Alive⚜️"
