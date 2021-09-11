__author__ = 'Rubiel G. labarta'

from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Hola humano')

if __name__ == '__main__':
    updater =  Updater(token='token de tu api', use_context=True)
    dp = Updater.dispatcher
    # add handler
    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()