#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lord.py
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
import Databank.datamanager as dm
import Utility.logger as log

def vassal(update, context):
    try:
        idu = update.message.from_user.id
        nicku = update.message.from_user.username
        subject = (nicku or str(idu))
        lords = (dm.dataread("config"))["lords"]
        if idu not in lords:
            update.message.reply_text("Non sei autorizzato.",
                quote = True)
        elif len(context.args) == 0:
            if update.message.reply_to_message:
                ida = update.message.reply_to_message.from_user.id
                nicka = update.message.reply_to_message.from_user.username
                namea = update.message.reply_to_message.from_user.first_name
                addressee = (nicka or namea)
                msgida = update.message.reply_to_message.message_id
                chatid = update.message.chat.id
                vassals = (dm.dataread("vassals"))["vassals"]
                vassals.append(ida)
                vassals = list(dict.fromkeys(vassals))
                newdb = {"vassals": vassals}
                dm.datawrite("vassals", newdb)
                context.bot.send_message(chat_id = chatid,
                    reply_to_message_id = msgida,
                    text = "%s adesso è un Vassallo."%addressee,
                    parse_mode = "markdown")
                log.a("%s ha vassallizzato %s, nm.: %s"%(subject, addressee, str(ida)))
            else:
                update.message.reply_text("Devi rispondere a un messaggio.",
                    quote = True)
        else:
            listids = [int(i) for i in context.args]
            vassals = (dm.dataread("vassals"))["vassals"]
            for ids in listids:
                vassals.append(ids)
            vassals = list(dict.fromkeys(vassals))
            newdb = {"vassals": vassals}
            dm.datawrite("vassals", newdb)
            update.message.reply_text("L'utente nm. %s ora fa parte dei Vassalli."%str(listids),
                quote = True)
            log.a("%s ha vassallizzato %s"%(subject, str(context.args)))
    except Exception as err:
        log.e(err)

def debase(update, context):
    try:
        idu = update.message.from_user.id
        nicku = update.message.from_user.username
        subject = (nicku or str(idu))
        lords = (dm.dataread("config"))["lords"]
        if idu not in lords:
            update.message.reply_text("Non sei autorizzato.",
                quote = True)
        elif len(context.args) == 0:
            if update.message.reply_to_message:
                ida = update.message.reply_to_message.from_user.id
                nicka = update.message.reply_to_message.from_user.username
                namea = update.message.reply_to_message.from_user.first_name
                addressee = (nicka or namea)
                msgida = update.message.reply_to_message.message_id
                chatid = update.message.chat.id
                vassals = (dm.dataread("vassals"))["vassals"]
                vassals = list(dict.fromkeys(vassals))
                vassals.remove(ida)
                vassals = list(dict.fromkeys(vassals))
                newdb = {"vassals": vassals}
                dm.datawrite("vassals", newdb)
                context.bot.send_message(chat_id = chatid,
                    reply_to_message_id = msgida,
                    text = "%s adesso non è più un Vassallo."%addressee,
                    parse_mode = "markdown")
                log.a("%s ha degradato %s, nm.: %s"%(subject, addressee, str(ida)))
            else:
                update.message.reply_text("Devi rispondere a un messaggio.",
                    quote = True)
        else:
            listids = [int(i) for i in context.args]
            vassals = (dm.dataread("vassals"))["vassals"]
            vassals = list(dict.fromkeys(vassals))
            for ids in listids:
                vassals.remove(ids)
            vassals = list(dict.fromkeys(vassals))
            newdb = {"vassals": vassals}
            dm.datawrite("vassals", newdb)
            update.message.reply_text("L'utente nm. %s ora non fa più parte dei Vassalli."%str(context.args),
                quote = True)
            log.a("%s ha degradato %s"%(subject, str(context.args)))
    except Exception as err:
        log.e(err)
