import requests
import os
import json
import re


nanonets_auth = os.environ['NANONETS_KEY']
TOTAL_AMT_STR = "Total_Amount"
VALUE = "ocr_text"

url = os.environ['url']

def nanonetOcr():
  image_path = os.getcwd() + "/images/image.jpg"
  data = {'file': open(image_path, 'rb')}

  response = requests.post(url, auth=requests.auth.HTTPBasicAuth(nanonets_auth, ''), files=data)

  total = parseAmount(getValueFromJson(response.text))

  return total

def parseAmount(totalAmount):
  rawdata2 = re.sub('[^0-9,.]', '', totalAmount)
  amountinnums = float(rawdata2)
  return amountinnums

def getValueFromJson(json_str):

  total_amt_index = -1
  raw_data = json.loads(json_str)
  data = raw_data["result"][0]["prediction"]
  for i in range(0, len(data)):
    if data[i]['label'] == TOTAL_AMT_STR:
      total_amt_index = i

  print("TOTAL AMT STR IS " + data[total_amt_index][VALUE])

  return data[total_amt_index][VALUE]

