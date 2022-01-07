def help(update, context):
  """Send a message when the command /help is issued."""
  update.callback_query.message.edit_text('Help!')
  