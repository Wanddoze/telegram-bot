# -*- coding: utf-8 -*-
import re
from telegram import ChatAction
from helper import crawler

import pprint
pp = pprint.PrettyPrinter(indent=2)

URL = 'http://www.reddit.com'

def normalize_text_to_search(text):
    print('normalize_text_to_search')
    pattern = re.compile('/nadaprafazer ', re.IGNORECASE)
    text_new = pattern.sub('', text).replace(' ', '')
    return text_new

def get_result_by_reddits(subReddits):
    results = []
    for subReddit in subReddits:
        print( type(subReddit))
        url_get = URL + '/r/' + subReddit
        cur_result = crawler.get_data(url_get)
        if(cur_result!=None):
            results.extend(cur_result)
    return results

def handler(bot, update):
    message = update.message
    text = message.text
    bot.sendChatAction(chat_id=message.chat_id,
                   action=ChatAction.TYPING)
    bot.sendChatAction(chat_id=message.chat_id,
                   action=ChatAction.TYPING)
    cmd = normalize_text_to_search(text)
    if cmd.endswith(';'):
        cmd = cmd[:-1]
    subReddits = cmd.split(';')
    results = get_result_by_reddits(subReddits)
    if(len(results)==0):              
        bot.sendMessage(message.chat_id,'Não encontramos nada bombando para estes tópicos, tente gatinhos(cats)')
    else:
        bot.sendMessage(message.chat_id, '\U0001F4A3')
    for result in results:
        payload = '''
            \n
            Thread: {title} 
            \nLink: {link} 
            \nNo subreddit: https://www.reddit.com{subreddit} 
            \nVeja os comentários em: https://www.reddit.com/{comments} 
            \nEla tem  {upvotes} upvotes'
            \n
        '''.format(title=result['title']
            , link=result['link']
            , subreddit=result['subreddit']
            , comments=result['comments']
            , upvotes=result['upvotes'])
        bot.sendMessage(message.chat_id, payload)