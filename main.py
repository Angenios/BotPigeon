#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2020 Lord Pigeon <angeloxd1@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import os, math, re, random, sys, subprocess, errno, signal
import time as t
from telegram.ext import *
from telegram.ext.dispatcher import run_async
import Utility.logger as log
from Core.commands import *
from Core.triggers import *
from Core.inlinemode import *
from Core.janitor import *
from Core.lord import *
import Databank.datamanager as dm
from Media.extractor import *
from Extra.dht11 import * # Comment if you don't have a Raspberry Pi with a DHT11 sensor

log.init(mode=1)

def main():
    updater = Updater(dm.dataread("config")["token"], use_context=True)
    dp = updater.dispatcher
    ch = CommandHandler
    mh = MessageHandler
    
    # Very important, as soon as you set your ID in the config.yaml file send this command in the private chat with the bot
    dp.add_handler(ch("syncmedia", syncmedia))
    
    dp.add_handler(ch("start", start))
    dp.add_handler(ch("help", helpcom))
    dp.add_handler(ch("info", info))
    dp.add_handler(ch("userid", userid))
    dp.add_handler(ch("groupid", groupid))
    
    dp.add_handler(ch("vassal", vassal))
    dp.add_handler(ch("debase", debase))
    
    # Comment if you don't have a Raspberry Pi with a DHT11 sensor
    dp.add_handler(ch("envdht", envdht))
    
    dp.add_handler(mh(Filters.text & Filters.update.messages, triggers))
    
    dp.add_handler(InlineQueryHandler(inlineresults))
    dp.add_handler(ChosenInlineResultHandler(inlinelog))
    
    dp.add_handler(mh(Filters.status_update.new_chat_members, welcome))
    
    log.i("Bot %s avviato"%updater.bot.username)
    updater.start_polling(clean=False)
    
    updater.idle()

if __name__ == '__main__':
    os.system("clear")
    log.i("Bot avviato")
    log.i("Premi CTRL+C per fermare")
    main()
    log.i("Bot fermato")
