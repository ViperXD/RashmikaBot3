# usr/bin/coding/
# -*- coding: utf-8 -*-
# (c) ALEN TL

from sqlalchemy import Column, Numeric, String

from RashmikaBot.modules.sql import BASE, SESSION


class forcesubscribe(BASE):
    __tablename__ = "forcesubscribe"
    chat_id = Column(Numeric, primary_key=True)
    channel = Column(String)

    def __init__(self, chat_id, channel):
        self.chat_id = chat_id
        self.channel = channel


forcesubscribe.__table__.create(checkfirst=True)


def fs_settings(chat_id):
    try:
        return (
            SESSION.query(forcesubscribe)
            .filter(forceSubscribe.chat_id == chat_id)
            .one()
        )
    except:
        return None
    finally:
        SESSION.close()


def add_channel(chat_id, channel):
    adder = SESSION.query(forcesubscribe).get(chat_id)
    if adder:
        adder.channel = channel
    else:
        adder = forcesubscribe(chat_id, channel)
    SESSION.add(adder)
    SESSION.commit()


def disapprove(chat_id):
    rem = SESSION.query(forcesubscribe).get(chat_id)
    if rem:
        SESSION.delete(rem)
        SESSION.commit()