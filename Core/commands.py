#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  commands.py
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
import Utility.logger as log

def start(update, context):
    try:
        if len(context.args) == 0:
            idu = update.message.from_user.id
            nicku = update.message.from_user.username
            subject = (nicku or str(idu))
            nameu = update.message.from_user.first_name
            update.message.reply_text("Ciao, %s, io sono il bot personale di @LordPigeon! \nDigita /help per una guida."%(nicku or nameu),
                parse_mode = "markdown",
                quote = True)
            log.a("%s ha usato /start"%subject)
        elif "help" in context.args:
            helpall(update, context)
        elif "helpinline" in context.args:
            helpinline(update, context)
        elif "info" in context.args:
            info(update, context)
    except Exception as err:
        log.e(err)

def helpall(update, context):
    try:
        idu = update.message.from_user.id
        nicku = update.message.from_user.username
        subject = (nicku or str(idu))
        tryinlinekey = [[InlineKeyboardButton(
            text = "Prova la modalità inline!",
            switch_inline_query_current_chat = "")]]
        helpkeyboard = InlineKeyboardMarkup(tryinlinekey)
        update.message.reply_text("<b>Comandi</b> "
                "\n/start - <i>Mi avvio</i> "
                "\n/help - <i>Invio questa lista</i> "
                "\n/info - <i>Invio varie informazioni sul bot</i> "
                "\n/userid - <i>Se utilizzato rispondendo al messaggio di un utente, mostro la sua nematrice</i> " 
                "\n/groupid - <i>Se utilizzato in un gruppo, mostra la nematrice del gruppo</i> "
                "\n/envdht* - <i>Rilevo la temperatura e l'umidità della mia camera da letto</i> "
                "\n<s>/distance* - <i>Elaboro la distanza tra il sensore HC-SR04 e un oggetto qualsiasi</i></s> "
                "\n"
                "\n<b>Trigger</b> "
                "\n<code>I'm Piccione</code> - <i>Risponderò con un meme o con una canzone</i> "
                "\n<code>I fuck your padre</code> - <i>Continuero la citazione di @PadriFibra</i> "
                "\n<code>Kosovo</code> - <i>Risponderò con una canzone, una volta ogni tanto nei gruppi</i> "
                "\n<code>Senate</code> - <i>Se mi va, reclamerò la mia autorità</i> "
                "\n<code>Buonsalve</code> - <i>Ti ricambio il saluto o lo riporto ad altri</i> "
                "\n<code>Bot Pigeon, attivazione</code> - <i>Reagirò con un segnale di avvio</i> "
                "\n"
                "\nI comandi seguiti dall'asterisco sono disponibili solo ai Vassalli (utenti autorizzati da Lord Pigeon). ",
            parse_mode = "HTML",
            reply_markup = helpkeyboard,
            quote = True)
        log.a("%s ha usato /help"%subject)
    except Exception as err:
        log.e(err)

def helpinline(update, context):
    try:
        idu = update.message.from_user.id
        nicku = update.message.from_user.username
        subject = (nicku or str(idu))
        trymekey = [[InlineKeyboardButton(
            text = "Provami!",
            switch_inline_query = "")]]
        helpinlinekeyboard = InlineKeyboardMarkup(trymekey)
        update.message.reply_text("*Lista delle funzioni inline*: "
                "\n1) `You know the rules and so do I` - _Per un triste addio a un picciotto disobbediente._ "
                "\n2) `Meteo` - _Scrivi il nome di una località e clicca per vederne le previsioni metereologiche._ "
                "\n3) `Formatta in HTMl` - _Scrivi un testo con tag HTML che siano compatibili con Telegram per vedere il risultato._ "
                "\n4) `Formatta in maiuscolo` - _Utile se vuoi ottenere rapidamente lettere accentate maiuscole da PC._ "
                "\n5) `Tripcode` - _Scrivi un messaggio e alla fine inserisci una #password (che inizi con l'hashtag) e il bot cripterà la tua password, utile nei gruppi anonimi._ "
                "\n"
                "\nEvita di usare il cancelletto (#) alla fine se vuoi usare le prime quattro funzioni.",
            parse_mode = "markdown",
            reply_markup = helpinlinekeyboard,
            quote = True)
        log.a("%s ha usato /start helpinline"%subject)
    except Exception as err:
        log.e(err)

def helpcom(update, context):
    try:
        typechat = update.message.chat.type
        if typechat == "private":
            helpall(update, context)
        else:
            idu = update.message.from_user.id
            nicku = update.message.from_user.username
            subject = (nicku or str(idu))
            titlechat = update.message.chat.title
            clickhelpkey = [[InlineKeyboardButton(
                text = "Clicca qui!",
                url = f"https://telegram.me/{context.bot.username}?start=help")]]
            helpgroupkeyboard = InlineKeyboardMarkup(clickhelpkey)
            update.message.reply_text("Avviami in chat privata per leggere le istruzioni.",
                parse_mode = "markdown",
                reply_markup = helpgroupkeyboard,
                quote = True)
            log.a("%s ha usato /help in %s"%(subject, titlechat))
    except Exception as err:
        log.e(err)

def info(update, context):
    try:
        idu = update.message.from_user.id
        nicku = update.message.from_user.username
        subject = (nicku or str(idu))
        typechat = update.message.chat.type
        if typechat == "private":
            update.message.reply_text("Io sono il bot personale di @LordPigeon e "
                    "sono stato programmato in Python grazie all'aiuto di vari amici: "
                    "\n• @Kaikyu "
                    "\n• @canebrutto "
                    "\n• @i7_8700k "
                    "\n• @hugihadein \n"
                    '\nFunziono su di un Raspberry Pi 3 Model B grazie a <a href="https://python-telegram-bot.org/">python-telegram-bot</a> e '
                    'a <a href="https://github.com/KaikyuLotus/kitsu-maker-bot/blob/master/Utils/Logger.py">un logger di Kaikyu</a>. ',
                parse_mode = "HTML",
                disable_web_page_preview = True,
                quote = True)
            log.a("%s ha usato /info"%subject)
        else:
            titlechat = update.message.chat.title
            clickinfokey = [[InlineKeyboardButton(
                text = "Clicca qui!",
                url = f"https://telegram.me/{context.bot.username}?start=info")]]
            infogroupkeyboard = InlineKeyboardMarkup(clickinfokey)
            update.message.reply_text("Avviami in chat privata per leggere più informazioni su di me.",
                parse_mode = "markdown",
                reply_markup = infogroupkeyboard,
                quote = True)
            log.a("%s ha usato /info in %s"%(subject, titlechat))
    except Exception as err:
        log.e(err)

def userid(update, context):
    try:
        idu = update.message.from_user.id
        nicku = update.message.from_user.username
        subject = (nicku or str(idu))
        if update.message.reply_to_message:
            ida = update.message.reply_to_message.from_user.id
            nicka = update.message.reply_to_message.from_user.username
            namea = update.message.reply_to_message.from_user.first_name
            addressee = (nicka or namea)
            msgida = update.message.reply_to_message.message_id
            chatid = update.message.chat.id
            context.bot.send_message(chat_id = chatid,
                reply_to_message_id = msgida,
                text = "Nematrice di %s: \n`%s`"%(addressee, str(ida)),
                parse_mode = "markdown")
            log.a("%s ha scoperto che la nm. di %s è %s"%(subject, addressee, str(ida)))
        else:
            update.message.reply_text("Devi rispondere a un messaggio per usare questo comando. ",
                parse_mode = "markdown",
                quote = True)
            log.a("%s ha scoperto che deve rispondere a un messaggio per usare /userid"%subject)
    except Exception as err:
        log.e(err)

def groupid(update, context):
    try:
        idu = update.message.from_user.id
        nicku = update.message.from_user.username
        subject = (nicku or str(idu))
        chatid = update.message.chat.id
        typechat = update.message.chat.type
        if typechat == "group":
            titlechat = update.message.chat.title
            update.message.reply_text("La nematrice del gruppo è: \n`%s`"%str(chatid),
                parse_mode = "markdown",
                quote = True)
            log.a("%s ha scoperto che la nematrice del gruppo \"%s\" è: %s"%(subject, titlechat, str(chatid)))
        elif typechat == "supergroup":
            titlechat = update.message.chat.title
            update.message.reply_text("La nematrice del supergruppo è: \n`%s`"%str(chatid),
                parse_mode = "markdown",
                quote = True)
            log.a("%s ha scoperto che la nematrice del supergruppo \"%s\" è: %s"%(subject, titlechat, str(chatid)))
        else:
            update.message.reply_text("Devi essere in un gruppo per usare questo comando. ",
                parse_mode = "markdown",
                quote = True)
            log.a("%s ha scoperto che dev'essere in un gruppo per usare /groupid"%subject)
    except Exception as err:
        log.e(err)
