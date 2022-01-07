#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler
# from plugins.interface import interface
from plugins.interface import start, help, error, echo, date, queryhandler
from plugins.imageprocessing import image
from telegram import *

# Enable logging
logging.basicConfig(format='%(asctime)s\n - %(name)s\n - %(levelname)s\n - %(message)s\n',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    my_secret = os.environ['my_secret']
    updater = Updater(my_secret, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # command handlers
    dp.add_handler(CommandHandler("start", start.start))
    dp.add_handler(CommandHandler("help", help.help))
    dp.add_handler(CommandHandler("date", date.getDateTime))

    # message handlers
    dp.add_handler(MessageHandler(Filters.text, echo.echo))
    dp.add_handler(MessageHandler(Filters.photo, image.imageHandler))
    
    # callback query handlers
    dp.add_handler(CallbackQueryHandler(queryhandler.queryHandler))

    # errors
    dp.add_error_handler(error.error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
