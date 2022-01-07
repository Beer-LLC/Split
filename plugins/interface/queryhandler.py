from . import help

simplelist = ["bcm $5", "durian $200", "derp $3.14"]

def queryHandler(update, context):
    query = update.callback_query.data
    update.callback_query.answer()
    
    if "like" in query:
      context.bot.send_message(chat_id=update.effective_chat.id, text = "1")
      help.help(update, context)
    elif "dislike" in query:
      context.bot.send_message(chat_id=update.effective_chat.id, text = "booooooo")
      help.help(update, context)
      
