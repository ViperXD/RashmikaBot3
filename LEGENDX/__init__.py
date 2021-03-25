#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ALEN TL

from RashmikaBot.events import register as LEGENDX22
from RashmikaBot import telethn as bot
from RashmikaBot import API_ID, API_HASH
from RashmikaBot.events import *
from telethon import TelegramClient
from telethon.sessions import StringSession

import os
STRING_SESSION = os.environ.get("STRING_SESSION")
if STRING_SESSION:
    user = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
else:
     print ("please add StringSession var")

try:
     user.start()
except Exception as e:
     print(e)
        

