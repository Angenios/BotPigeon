#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  inlinemode.py
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
import re
import Databank.datamanager as dm
from Utility.codegen import tripcode
import Utility.logger as log

def inlineresults(update, context):
    try:
        query = update.inline_query.query
        if not query:
            wtrquest = "New York"
            formatquest = "Nessun testo trovato, riprovare."
        else:
            wtrquest = str((re.compile(r'<[^>]+>')).sub("",query))
            formatquest = query
        results = [
            InlineQueryResultVideo(
                id = "RickAstley",
                title = "You know the rules and so do I",
                mime_type = "video/mp4",
                video_url = dm.dataread("media")["Inline"]["VideoRickAstley"],
                thumb_url = dm.dataread("media")["Inline"]["ThumbRickAstley"]
                ),
            InlineQueryResultPhoto(
                id = "Meteo",
                title = "Meteo di %s"%wtrquest,
                photo_url = str("https://wttr.in/"+wtrquest.replace(" ", "+")+"_lang=it.png?v=1"),
                thumb_url = str("https://wttr.in/"+wtrquest.replace(" ", "+")+"_0pq_lang=it.png?v=1")
                ),
            InlineQueryResultArticle(
                id = "FormatHTML",
                title = "Formatta in HTML",
                input_message_content = InputTextMessageContent(formatquest, parse_mode="HTML")
                ),
            InlineQueryResultArticle(
                id = "FormatUp",
                title = "Formatta in maiuscolo",
                input_message_content = InputTextMessageContent(formatquest.upper())
                )]
        if not query:
            pass
        elif re.search(r'<[^>]+>', query):
            results.clear()
            results.append(InlineQueryResultArticle(
                id = "FormatHTML",
                title = "Formatta in HTML",
                input_message_content = InputTextMessageContent(query, parse_mode = "HTML")))
        elif bool(re.match("#",query.split()[-1]))==False:
            pass
        else:
            results.clear()
            questlist = query.split() # Divides the query into a list
            txtmsg = questlist[:-1] # Takes the message before the hashtag
            upass = questlist[-1][1:] # Takes the password after the hashtag
            txtmsg.append(tripcode(upass, 8)) # Appends the encrypted password to the message
            cryptmsg = " ".join(txtmsg) # Joins the final list into a string
            results.append(InlineQueryResultArticle(
                id = "Tripcode",
                title = "Tripcode",
                input_message_content = InputTextMessageContent(cryptmsg)
                ))
        update.inline_query.answer(results,
            cache_time = 4,
            switch_pm_text = "Leggi le istruzioni in chat privata",
            switch_pm_parameter = "helpinline")
    except Exception as err:
        log.e(err)

def inlinelog(update, context):
    try:
        idu = update.chosen_inline_result.from_user.id
        nicku = update.chosen_inline_result.from_user.username
        subject = (nicku or str(idu))
        query = update.chosen_inline_result.query
        loot = update.chosen_inline_result.result_id
        if not query:
            quest = str("")
        else:
            quest = str(": "+str(query))
        journal = str(str(loot)+quest)
        log.a("%s ha scelto inline %s"%(subject, journal))
    except Exception as err:
        log.e(err)
