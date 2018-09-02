#!/usr/bin/env python3.7

import requests
from datetime import datetime
from tg_token import token


class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = f'https://api.telegram.org/bot{token}/'
        print(self.api_url)

    def getUpdates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {
            'timeout': timeout,
            'offset': offset
            }
        response = requests.get(self.api_url + method, params)
        result_json = response.json()['result']
        return result_json

    def reply(self, chat_id, text):
        method = 'sendMessage'
        params = {
                'chat_id': chat_id,
                'text': text
                }
        response = requests.post(self.api_url + method, params)
        return response

    def getLastUpdate(self):
        get_result = self.getUpdates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result#[len(get_result)]
        return last_update


greet_bot = BotHandler(token)

greetings = ('hello', 'hi', 'greetings', 'wassup')

now = datetime.now()



def main():
    new_offset = None
    today = now.day
    hour = now.hour


    while True:
        greet_bot.getUpdates(new_offset)
        last_update = greet_bot.getLastUpdate()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6<= hour < 12:
            greet_bot.reply(last_chat_id, f'Good Morning {last_chat_name}')
            today +=1
        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.reply(last_chat_id, f'Good Afternoon {last_chat_name}')
            today += 1
        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.reply(last_chat_id, f'Good Evening  {last_chat_name}')
            today += 1

        new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
