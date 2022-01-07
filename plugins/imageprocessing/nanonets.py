import requests
import os

nanonets_auth = os.environ['NANONETS_KEY']

url = 'https://app.nanonets.com/api/v2/OCR/Model/2ec4855d-e179-4db0-99ce-ee294f37f067/LabelFile/'

def nanonetOcr():
  image_path = os.getcwd() + "/images/image.jpg"
  data = {'file': open(image_path, 'rb')}

  response = requests.post(url, auth=requests.auth.HTTPBasicAuth(nanonets_auth, ''), files=data)

  print(response.text)