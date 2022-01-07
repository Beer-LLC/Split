import datetime

def getDateTime(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(datetime.datetime.now())