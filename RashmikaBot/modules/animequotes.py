#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ALEN TL

import random

from telegram import Update
from telegram.ext import CallbackContext, run_async

import RashmikaBot.modules.animequotesstring as animequotesstring
from RashmikaBot import dispatcher
from RashmikaBot.modules.disable import DisableAbleCommandHandler


@run_async
def animequotes(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(animequotesstring.ANIMEQUOTES))


ANIMEQUOTES_HANDLER = DisableAbleCommandHandler("animequotes", animequotes)

dispatcher.add_handler(ANIMEQUOTES_HANDLER)
