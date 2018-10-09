# -*- coding: utf-8 -*-
from telegram import InlineQueryResultArticle, ChatAction, InputTextMessageContent, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import configparser
from commands import start, nothing_to_do, support, support_message, unknown
from telegram.ext import Updater

def main():
    print('# Configuring bot')
    config = configparser.ConfigParser()
    config.read_file(open('config.ini'))

    # Connecting to Telegram API
    # Updater retrieves information and dispatcher connects commands
    updater = Updater(token=config['DEFAULT']['token'])
    dispatcher = updater.dispatcher

    try:
        start_handler = CommandHandler('start', start.handler)
        dispatcher.add_handler(start_handler)
        support_handler = CommandHandler('support', support.handler)
        dispatcher.add_handler(support_handler)
        unknown_handler = MessageHandler([Filters.command], unknown.handler)
        dispatcher.add_handler(unknown_handler)
        support_msg_handler = MessageHandler([Filters.text], support_message.handler)
        dispatcher.add_handler(support_msg_handler)
    # Message handler must be the last one
    except Exception as e:
        print(e)
    # Start the Bot
    
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()