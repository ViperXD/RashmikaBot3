#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ALEN TL

import re
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os, sys
from RashmikaBot import DB_URI, RASHMIKA, telethn
if RASHMIKA == 1312054275:
   print ("RASHMIKA ADDED SIR ")
else:
   print ("YOU REMOVED RASHMIKA MANDANNA NOW SEE")
   os.execl(sys.executable, sys.executable, *sys.argv)
   telethn.disconnect()

def start() -> scoped_session:
    engine = create_engine(DB_URI, client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()
