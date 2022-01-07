from telegram import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup

def start(update, context):
    buttons = [[KeyboardButton("/help")], [KeyboardButton("randomPeopleText")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my bot!", reply_markup=ReplyKeyboardMarkup(buttons))
    buttons1 = [[InlineKeyboardButton("👍",callback_data="like")], [InlineKeyboardButton("👎",callback_data="dislike")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons1), text="Did you like the image?")
    update.message.reply_text('Hello! Please type /help for a list of commands to get started.')
    