#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ALEN TL

from telethon import custom, events, Button
import os,re
from RashmikaBot import telethn as bot
from RashmikaBot import telethn as tgbot
from RashmikaBot.events import register 
@register(pattern="/myinfo")
async def proboyx(event):
  button = [[custom.Button.inline("CHECK",data="information")]]
  await bot.send_message(event.chat, "YOUR INFORMATION",buttons=button)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
  try:
    boy = event.sender_id
    PRO = await bot.get_entity(boy)
    RASHMIKA = "YOUR DETAILS BY RASHMIKA MANDANNA \n"
    RASHMIKA += f"FIRST NAME : {PRO.first_name} \n"
    RASHMIKA += f"LAST NAME : {PRO.last_name}\n"
    RASHMIKA += f"YOU BOT : {PRO.bot} \n"
    RASHMIKA += f"RESTRICTED : {PRO.restricted} \n"
    RASHMIKA += f"USER ID : {boy}\n"
    RASHMIKA += f"USERNAME : {PRO.username}\n"
    await event.answer(RASHMIKA, alert=True)
  except Exception as e:
    await event.reply(f"{e}")
