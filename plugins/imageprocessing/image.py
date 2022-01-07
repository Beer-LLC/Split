try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = "tesseract"
os.environ["TESSDATA_PREFIX"] = "~/Split/tessdata"

# downloads the image into a file
def imageHandler(update, context):
  print("image upload start")
  file = update.message.photo[-1].get_file()
  # print ("file_id: " + str(update.message.photo.file_id))
  image = file.download('images/image.jpg')
  print("Image loaded successfully!\n")
  imageProcessing()

# processes image
def imageProcessing():
  print(pytesseract.get_languages(config=''))
  print(pytesseract.image_to_string(Image.open('images/image.jpg')))