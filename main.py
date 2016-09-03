#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
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
from db import select, insert, delete
import logging
from creditails import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Всем привет')


def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)


def help(bot, update):
    bot.sendMessage(update.message.chat_id,
                    text="Доступные комманды:\n	/showall - показывает все события\n /new - создать новое событие (\"Название(не важно сколько слов разделенные пробелами или любымзнаком кроме тире (-))\" - (знак тире) \"Описание (любое количество слов разделеное чем угодно)\"\n /rm - удаляет событие по номеру (Пример: /rm 1)\n /wai - покажет ваше имя фамилию и ник в телеграме\n /killbot - не делает нечего хорошего")


def fix(bot, update):
    bot.sendMessage(update.message.chat_id, text='fixed!')


def showall(bot, update):
    ololo = select()
    bot.sendMessage(update.message.chat_id, text='%s' % ololo)


def new(bot, update):
    string = ''.join(update.message.text)
    try:
        withOutCommand = string.split(" ", 1)[1]
    except:
        bot.sendMessage(update.message.chat_id, text='После /new надо чет написать=))')
    if "-" in withOutCommand:
        name = withOutCommand.split('-', 1)[0]
        description = withOutCommand.split('-', 1)[1]
        print (description)
    else:
        name = ''
        description = withOutCommand
        print(name)
    author = str(update.message.from_user.first_name) + ' ' + str(update.message.from_user.last_name) + ' ' + str(
    update.message.from_user.username)
    insert(name, description, author)
    showall(bot, update)


def rm(bot, update):
    string = ''.join(update.message.text)
    try:
        withOutCommand = string.split(" ", 1)[1]
    except:
        bot.sendMessage(update.message.chat_id, text='После /rm надо номер написать=))')
    try:
        delete(int(withOutCommand))
    except:
        bot.sendMessage(update.message.chat_id, text='Чет пошло не так')
    showall(bot, update)


def killbot(bot, update):
    bot.sendMessage(update.message.chat_id, text='Хуй тебе')


def killseal(bot, update):
    bot.sendMessage(update.message.chat_id, text='Хуй тебе')


def wai(bot, update):
    author = str(update.message.from_user.first_name) + ' ' + str(update.message.from_user.last_name) + ' ' + str(
        update.message.from_user.username)
    bot.sendMessage(update.message.chat_id, text='%s' % author)

def release(bot, update):
    bot.sendMessage(update.message.chat_id, text='Немного новых фич: появилось удаление событий (команда /rm) так же команда /new теперь воспринимает либой текст и добавились человеко читабельные ошибки. Читайте /help')

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("%s" % token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("fix", fix))
    dp.add_handler(CommandHandler("showall", showall))
    dp.add_handler(CommandHandler("new", new))
    dp.add_handler(CommandHandler("rm", rm))
    dp.add_handler(CommandHandler("wai", wai))
    dp.add_handler(CommandHandler("release", release))
    dp.add_handler(CommandHandler("killbot", killbot))
    dp.add_handler(CommandHandler("killseal", killseal))
    dp.add_handler(MessageHandler([Filters.text], echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
