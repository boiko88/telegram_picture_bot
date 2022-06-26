import api as key
import responses as R
from telegram.ext import *

# The actual name of the bot to find it in telegram - PersonalExpenseCalculatorBot

print("bot launched")


def start_command(update, context):
    update.message.reply_text("Type something to launch the bot!")


def help_command(update, context):
    update.message.reply_text(
        "If you need help you can have a look at all the main commands of the bot to do what you want.")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.response_function(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Your last message {update} caused error {context.error}")


def main():
    updater = Updater(key.my_bot_api_key, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
