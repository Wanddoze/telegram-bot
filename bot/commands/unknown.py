# -*- coding: utf-8 -*-
from telegram import ChatAction

def handler(bot, update):
    """
        Placeholder command when the user sends an unknown command.
    """
    bot.sendChatAction(chat_id=update.message.chat_id,
                action=ChatAction.TYPING)
    msg = "Sorry, I don't know what you're asking for."
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)