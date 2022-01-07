from telegram import ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup

def start(update, context):
    markup = ReplyKeyboardMarkup(keyboard=[['/help'],["File", "Audio"]],resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text = "temp",reply_markup=markup)
    buttons1 = [[InlineKeyboardButton("👍",callback_data="like")], [InlineKeyboardButton("👎",callback_data="dislike")]]
    context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons1), text="Did you like the image?")
   #  update.message.reply_text('Hello! Please type /help for a list of commands to get started.')
    