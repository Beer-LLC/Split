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
  print("image upload start")
  file = update.message.photo[-1].get_file()
  # print ("file_id: " + str(update.message.photo.file_id))
  file.download('images/image.jpg')
  print("Image loaded successfully!\n")
  nanonets.nanonetOcr()
  # imageProcessing()

# processes image
def imageProcessing():
  print(pytesseract.get_languages(config=''))
  tic = time.perf_counter()
  print(pytesseract.image_to_string(Image.open('images/image.jpg'), lang='eng'))  
  toc = time.perf_counter()
  print(f"OCR took {toc - tic:0.4f} seconds")