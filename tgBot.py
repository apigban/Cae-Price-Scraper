#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

"""Bot to retrieve telegram message.

This Bot uses the Updater class to handle the bot.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from tg_token import bot_token
import logging
from inputValidator import cmdValidator
import pageQueue

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def get_userinfo(bot, update):
    userid = update.message.from_user.id
    user = update.message.from_user.first_name
    messageid = update.message.message_id
    update.message.reply_text(f'Hi {user}!')

    return user, userid, messageid

@pageQueue.redisWrite
def get_price(bot, update, **product):
    """Extract the product from user message using module inputValidator's function cmdValidator"""

    requester, user_id, request_id = get_userinfo(bot, update)

    grocery_item, query_status, time_stamp = cmdValidator(product['args'])

    if query_status == 'empty':
        update.message.reply_text('YO! you\'ve entered no grocery item for me to find. \n\nPlease try again with /getprice <item> \n\n example:\n   /getprice strawberries')

    elif query_status == 'nonalpha':

        update.message.reply_text('YO! Can\'t understand what you typed, please use letters. \n\nPlease try again with /getprice <item> \n\n example:\n   /getprice strawberries')

    else:

        update.message.reply_text(f'Looking for the price of {grocery_item}... Please wait...')


    #product_query = ' '.join()
#   bot.send_message(chat_id=update.message.chat_id, text=f'looking for the lowest price of {product_query}')
    #update.message.reply_text(f'Looking for the lowest price of {product_query}')
    return grocery_item, query_status, time_stamp, requester, request_id


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(bot_token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("getprice", get_price, pass_args=True))
    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))
    #dp.add_handler(MessageHandler(Filters.text, getprice))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
