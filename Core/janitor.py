#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  janitor.py
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
import Utility.logger as log

def welcome(update, context):
    try:
        titlechat = update.message.chat.title
        if update.message.new_chat_members[-1].id == context.bot.id:
            idu = update.message.from_user.id
            nicku = update.message.from_user.username
            subject = (nicku or str(idu))
            nameu = update.message.from_user.first_name
            update.message.reply_text("Grazie per avermi aggiunto, %s!"%(nicku or nameu),
                quote = True)
            log.i("%s mi ha aggiunto a %s"%(subject, titlechat))
        else:
            idc = update.message.new_chat_members[-1].id
            nickc = update.message.new_chat_members[-1].username
            client = (nickc or str(idc))
            namec = update.message.new_chat_members[-1].first_name
            update.message.reply_text("Buonsalve e benvenuto/a, %s!"%(nickc or namec),
                quote = True)
            log.i("Ho dato il benvenuto a %s in %s"%(client, titlechat))
    except Exception as err:
        log.e(err)
