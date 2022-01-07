def echo(update, context):
  """Echo the user message."""
  update.message.reply_text(update.message.text)