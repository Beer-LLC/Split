try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
import time
from . import nanonets
pytesseract.pytesseract.tesseract_cmd = "tesseract"
os.environ["TESSDATA_PREFIX"] = os.getcwd() + "/tessdata/"

# downloads the image into a file
def imageHandler(update, context):
  # if conditional at the start to check for integer
  print("image upload start")
  file = update.message.photo[-1].get_file()
  if update.message.caption is None:
    photocaption = "1"
  else:
    photocaption = update.message.caption
  persons = nanonets.parseAmount(photocaption)
  print(persons)
  file.download('images/image.jpg')
  print("Image loaded successfully!\n")
  total_amt = nanonets.nanonetOcr()
  # get user input integer
  individual_amt = total_amt/persons
  indiv_amt_str = "each person pays $" + str(round(individual_amt,2))
  print(indiv_amt_str)
  update.message.reply_text(indiv_amt_str)