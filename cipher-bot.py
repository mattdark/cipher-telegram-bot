#!/usr/bin/env python3
# python-telegram-bot https://python-telegram-bot.org/
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import operator
from caesar import caesar

updater = Updater(token='391696914:AAECRPFaf20X7N8qtyCJ0gwAC-7_o1SesgE')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, I can encrypt text using Caesar cipher!") # Welcome message

# /help command
def help(bot, update):
    # Menu options
    keyboard = [[InlineKeyboardButton("Instructions", callback_data='1')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup) # Menu title

# Function that prints information according to the selected option
def button(bot, update):
    query = update.callback_query
    if query.data == '1':
        text = "Introduce text and key separated by comma \n Example: This is just a text,3" # Intructions
    bot.editMessageText(text = text,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)

# Function that encrypt text using Caesar cipher
def cipher(bot, update):
    message, key = update.message.text.split(",")
    message=list(message.lower())
    caesar(message, key)
    message="".join(message)
    bot.send_message(chat_id=update.message.chat_id, text=message)

start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
cipher_handler = MessageHandler(Filters.text, cipher)
button_handler = CallbackQueryHandler(button)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(button_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(cipher_handler)

updater.start_polling()
