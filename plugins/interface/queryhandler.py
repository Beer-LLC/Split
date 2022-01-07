from telegram import ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
from . import help

simplelist = ["bcm $5", "durian $200", "derp $3.14"]

def queryHandler(update, context):
    query = update.callback_query.data
    update.callback_query.answer()
    
    if "dislike" in query:
      help.help(update, context)
    elif "like" in query:
      help.help(update, context)