#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dht11.py
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
from telegram import *
import Adafruit_DHT
import time as t
import Databank.datamanager as dm
import Utility.logger as log

def envdht(update, context):
    try:
        idu = update.message.from_user.id
        nicku = update.message.from_user.username
        subject = (nicku or str(idu))
        chatid = update.message.chat.id
        nobles = dm.dataread("config")["lords"] + dm.dataread("vassals")["vassals"]
        if idu not in nobles:
            update.message.reply_text("Non sei autorizzato, entra nella @RepubblicaPiccionesca per richiedere il vassallaggio.", 
                quote = True)
            log.a("%s non ha le autorizzazioni necessarie per /envdht"%subject)
        else:
            msgidu = update.message.message_id
            log.dht("Misurazione di temperatura e umidità avviata")
            reportmsg = context.bot.sendMessage(chat_id = chatid, 
                reply_to_message = msgidu, 
                text = "*Misurazione avviata*", 
                parse_mode = "markdown", 
                quote = True).message_id
            context.bot.send_chat_action(chat_id = chatid, 
                action="FIND_LOCATION")
            try:
                log.dht("In elaborazione...")
                context.bot.editMessageText(chat_id = chatid, 
                    message_id = reportmsg, 
                    text = "_In elaborazione..._", 
                    parse_mode = "markdown")
                datapin = int(dm.dataread("extra")["dht11"])
                humidity, temperature = Adafruit_DHT.read_retry(11, datapin)
                log.dht("Temperatura {0:0.1f} - Umidità {1:0.1f}".format(temperature, humidity))
                try:
                    context.bot.editMessageText(chat_id = chatid, 
                        message_id = reportmsg, 
                        text = (("*RISULTATO OTTENUTO*\n_Sensore_: `DHT11`\n_Temperatura_: `{0:0.1f}℃` \n_Umidità_: `{1:0.1f}%`").format(temperature, humidity)), 
                        parse_mode = "markdown")
                    log.a("%s ha provato il sensore DHT11"%subject)
                except:
                    log.e(err)
            except Exception as err:
                GPIO.setmode(GPIO.BOARD)
                errorledpin = int(dm.dataread("extra")["errorled"])
                GPIO.setup(errorledpin, GPIO.OUT)
                GPIO.output(errorledpin, GPIO.HIGH)
                t.sleep(2)
                GPIO.cleanup()
                context.bot.editMessageText(chat_id = chatid, 
                    message_id = reportmsg, 
                    text = "Mi dispiace, il sensore di temperatura e umidità ha avuto qualche problema. "
                        "Contatta @LordPigeon per segnalare l'accaduto.")
                log.a("%s NON ha potuto provare il sensore DHT11 per il seguente errore:"%subject)
                log.e(err)
    except Exception as err:
        log.e(err)
