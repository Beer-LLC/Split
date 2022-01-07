import logging

def error(update, context):
  logger = logging.getLogger(__name__)
  """Log Errors caused by Updates."""
  logger.warning('Update "%s" caused error "%s"', update, context.error)