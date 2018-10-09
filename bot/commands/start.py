# -*- coding: utf-8 -*-
from telegram import ChatAction, KeyboardButton, ReplyKeyboardMarkup

def handler(bot, update):
    """
        Shows an welcome message and help info about the available commands.
    """
    me = bot.get_me()
    bot.sendChatAction(chat_id=update.message.chat_id,
                   action=ChatAction.TYPING)
    # Welcome message
    msg = "Hello!\n"
    msg += "I'm {0} and I came here to help you.\n".format(me.first_name)
    msg += "What would you like to do?\n\n"
    msg += "/support - Opens a new support ticket\n"
    msg += "/settings - Settings of your account\n\n"
    # Commands menu
    main_menu_keyboard = [[KeyboardButton('/support')],
                          [KeyboardButton('/settings')],
                          [KeyboardButton('/NadaPraFazer')]
                        ]
    reply_kb_markup = ReplyKeyboardMarkup(main_menu_keyboard,
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)
    # Send the message with menu
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg,
                     reply_markup=reply_kb_markup)