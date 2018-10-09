# -*- coding: utf-8 -*-
from telegram import ChatAction

def handler(bot, update):
    """
        Receives a message from the user.

        If the message is a reply to the user, the bot speaks with the user
        sending the message content. If the message is a request from the user,
        the bot forwards the message to the support group.
    """
    bot.sendChatAction(chat_id=update.message.chat_id,
                   action=ChatAction.TYPING)
    if update.message.reply_to_message and \
       update.message.reply_to_message.forward_from:
        # If it is a reply to the user, the bot replies the user
        bot.send_message(chat_id=update.message.reply_to_message
                         .forward_from.id,
                         text=update.message.text)
    else:
        # If it is a request from the user, the bot forwards the message
        # to the group
        bot.forward_message(chat_id=int(config['DEFAULT']['support_chat_id']),
                            from_chat_id=update.message.chat_id,
                            message_id=update.message.message_id)
        bot.send_message(chat_id=update.message.chat_id,
                         text="Give me some time to think. Soon I will return to you with an answer.")