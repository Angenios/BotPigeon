#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  extractor.py
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

def syncmedia(update, context):
    try:
        idu = update.message.from_user.id
        nicku = update.message.from_user.username
        subject = (nicku or str(idu))
        lords = dm.dataread("config")["lords"]
        if idu not in lords:
            update.message.reply_text("Non sei autorizzato.",
                quote = True)
        else:
            videorickastley = context.bot.send_video(chat_id = idu,
                video = open("Media/Inline/RickAstley/VideoRickAstley.mp4", "rb")
                ).video.file_id
            thumbrickastley = context.bot.send_video(chat_id = idu,
                video = open("Media/Inline/RickAstley/VideoRickAstley.mp4", "rb")
                ).video.thumb.file_id
            impiccione = context.bot.send_photo(chat_id = idu,
                photo = open("Media/Triggers/Impiccione/MemeImpiccione.jpg", "rb")
                ).photo[-1].file_id
            sonounpiccione = context.bot.send_audio(chat_id = idu,
                audio = open("Media/Triggers/Impiccione/Sono un piccione.mp3", "rb")
                ).audio.file_id
            kosovo = context.bot.send_voice(chat_id = idu,
                voice = open("Media/Triggers/Kosovo/PositivoKosovo.ogg","rb")
                ).voice.file_id
            senate = context.bot.send_voice(chat_id = idu,
                voice = open("Media/Triggers/Senate/PositivoSenate.ogg", "rb")
                ).voice.file_id
            newmedia = {"Inline": {"VideoRickAstley": videorickastley, "ThumbRickAstley": thumbrickastley}, "Triggers": {"Impiccione": impiccione, "Sonounpiccione": sonounpiccione, "Kosovo": kosovo, "Senate": senate}}
            dm.datawrite("media", newmedia)
            log.d(f"{subject} ha aggiornato i media")
    except Exception as err:
        log.e(err)
