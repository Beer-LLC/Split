from telegram import ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
from . import help

simplelist = ["bcm $5", "durian $200", "derp $3.14"]

def queryHandler(update, context):
    query = update.callback_query.data
    update.callback_query.answer()
    
    if "dislike" in query:
      # context.bot.send_message(chat_id=update.effective_chat.id, text = "1234")
      help.help(update, context)
    elif "like" in query:
      # context.bot.send_message(chat_id=update.effective_chat.id, text = "booooooo")
      help.help(update, context)
      
# def generateButtonArray(inputList):
#   buttonArray = []
#   for i in range(0,inputList.size()):
#     value = [InlineKeyboardButton("👍",callback_data="like")]