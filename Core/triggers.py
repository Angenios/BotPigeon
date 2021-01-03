#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  triggers.py
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
import re, random
import Databank.datamanager as dm
import Utility.logger as log

def triggers(update, context):
    try:
        idu = update.message.from_user.id
        nicku = update.message.from_user.username
        subject = (nicku or str(idu))
        nameu = update.message.from_user.first_name
        chatid = update.message.chat.id
        content = update.message.text
        cont = content.lower()
        gasha = [0, 0, 0, "pon"]
        
        if content == "Salve" and idu == 254166588:
            update.message.reply_text("e sane")
            log.a("Per Matteo Socrati le ragazze sono salve, ma per me sono pure sane")
            return
        
        if "Prova" in content and random.choice(gasha) == "pon":
            update.message.reply_text("Funziona!", quote = True)
            log.a("%s ha provato!"%subject)
            return
        
        regex = "i'+m p+i+c+c+i+o+n+e"
        if re.search(regex, cont):
            try:
                impiccione = dm.dataread("media")["Triggers"]["Impiccione"]
                meridiana = dm.dataread("media")["Triggers"]["Sonounpiccione"]
                ambiguity = [0, "0"]
                if random.choice(ambiguity) == 0:
                    update.message.reply_photo(photo = impiccione,
                        quote = True)
                    log.a("%s è un imPiccione"%subject)
                    return
                else:
                    update.message.reply_audio(audio = meridiana,
                        quote = True)
                    log.a("%s è un Piccione"%subject)
                    return
            except Exception as err:
                log.e(err)
        
        regex = "i f+u+c+k y+o+u+r p+a+d+r+e"
        if re.search(regex, cont):
            try:
                if update.message.reply_to_message:
                    ida = update.message.reply_to_message.from_user.id
                    nicka = update.message.reply_to_message.from_user.username
                    addressee = (nicka or str(ida))
                    msgida = update.message.reply_to_message.message_id
                    chatid = update.message.chat.id
                    context.bot.send_message(chat_id = chatid,
                        reply_to_message_id = msgida,
                        text = "He's my puttana ",
                        parse_mode = "markdown")
                    log.a("%s si fa il padre di %s"%(subject, addressee))
                    return
                else:
                    update.message.reply_text("He's my puttana ",
                        parse_mode = "markdown",
                        quote = True)
                    log.a("%s segue PadriFibra"%subject)
                    return
            except Exception as err:
                log.e(err)
        
        regex = "k+o+s+o+v+o"
        if re.search(regex, cont):
            try:
                typechat = update.message.chat.type
                kosovo = dm.dataread("media")["Triggers"]["Kosovo"]
                if typechat == "private":
                    update.message.reply_voice(kosovo,
                        caption = "Stay tuned, @PadriFibra!",
                        quote = True)
                    log.a("%s ha lodato il Kosovo"%subject)
                    return
                else:
                    if random.choice(gasha) == 0:
                        titlechat = update.message.chat.title
                        log.a("%s non ha lodato abbastanza il Kosovo in %s"%(subject, titlechat))
                    elif random.choice(gasha) == "pon":
                        update.message.reply_voice(kosovo,
                            caption = "Stay tuned, @PadriFibra!",
                            quote = True)
                        log.a("%s ha lodato il Kosovo"%subject)
                    return
            except Exception as err:
                log.e(err)
        
        regex = "s+e+n+a+t+e"
        if re.search(regex, cont):
            try:
                if random.choice(gasha) == "pon":
                    senate = dm.dataread("media")["Triggers"]["Senate"]
                    update.message.reply_voice(senate,
                        caption = '<i>I am the <a href="https://t.me/ErarioPiccioni">Senate</a>!</i>',
                        parse_mode = "HTML",
                        quote = True)
                    log.a("I am the Senate, not %s"%subject)
                    return
                else:
                    return
            except Exception as err:
                log.e(err)
        
        regex = "b+u+o+n+s+a+l+v+e"
        if re.search(regex, cont):
            try:
                if update.message.reply_to_message:
                    ida = update.message.reply_to_message.from_user.id
                    nicka = update.message.reply_to_message.from_user.username
                    addressee = (nicka or (str(ida)))
                    chatid = update.message.chat.id
                    msgida = update.message.reply_to_message.message_id
                    namea = update.message.reply_to_message.from_user.first_name
                    context.bot.sendMessage(text = "Buonsalve, %s"%(nicka or namea),
                        chat_id = chatid,
                        reply_to_message_id = msgida,
                        quote = True)
                    log.a("%s ha salutato %s"%(subject, addressee))
                    return
                else:
                    update.message.reply_text("Buonsalve, %s!"%(nicku or nameu),
                        quote = True)
                    log.a("Ho ricambiato il saluto a %s"%subject)
                    return
            except Exception as err:
                log.e(err)
        
        regex = "b+o+t p+i+g+e+o+n, a+t+t+i+v+a+z+i+o+n+e"
        if re.search(regex, cont):
            try:
                update.message.reply_text("Bot Pigeon, attivato!",
                    quote = True)
                log.a("%s ha attivato il bot!"%subject)
                return
            except Exception as err:
                log.e(err)
        
    except Exception as err:
        log.e(err)
