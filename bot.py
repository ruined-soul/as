import os import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = os.environ.get('TOKEN')
OWNER_ID = os.environ.get('OWNER_ID')

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello!')

def add_sudo(update: Update, context: CallbackContext):
    if update.effective_user.id == OWNER_ID:
        sudo_user_id = update.message.text.split(' ')[1]
        # Add sudo user to database or file
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Added {sudo_user_id} as sudo user')
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='You are not authorized to add sudo users')

def bye(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text='bye')

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('add_sudo', add_sudo))
    dp.add_handler(MessageHandler(Filters.text, bye))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
