# -*- coding: utf-8 -*-
from telegram import ChatAction

def handler(bot, update):
    """
        Sends the support message. Some kind of "How can I help you?".
    """
    bot.sendChatAction(chat_id=update.message.chat_id,
                action=ChatAction.TYPING)
    bot.send_message(chat_id=update.message.chat_id,
                     text="Please, tell me what you need support with :)")
    
