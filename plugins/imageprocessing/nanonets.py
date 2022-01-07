# from pykson import Pykson, JsonObject, StringField
import requests
import os
import json
import re


nanonets_auth = os.environ['NANONETS_KEY']
TOTAL_AMT_STR = "Total_Amount"
VALUE = "ocr_text"

url = 'https://app.nanonets.com/api/v2/OCR/Model/2ec4855d-e179-4db0-99ce-ee294f37f067/LabelFile/'

  
def nanonetOcr():
  image_path = os.getcwd() + "/images/image.jpg"
  data = {'file': open(image_path, 'rb')}

  response = requests.post(url, auth=requests.auth.HTTPBasicAuth(nanonets_auth, ''), files=data)
  
  total = parseAmount(getValueFromJson(response.text))

  return total
  # parses json string into a dict 
  # obj = json.loads(response.text)

def parseAmount(totalAmount):
  print("penis0")
  rawdata2 = re.sub('[^0-9,.]', '', totalAmount)
  print("penis1")
  amountinnums = float(rawdata2)
  print("penis2")
  return amountinnums

def getValueFromJson(json_str):
  # with open("example.json") as infile:
  #   data = json.load(infile)
  
  total_amt_index = -1
  raw_data = json.loads(json_str)
  data = raw_data["result"]["prediction"]
  print(data)
  print("QWEQEWQEQWEQWEQWEWQEWQ")
  for i in range(0, len(data)):
    if data[i]['label'] == TOTAL_AMT_STR:
      total_amt_index = i

  # class Payload(pykson.JsonObject):
  #   label = StringField()
  #   ocr_text = StringField()
  #   score = StringField()

  # payload = Pykson.from_json(json_str, Payload)

  print("@#$#@$%@#$%#%#%@%$$%#@%$@$%")

  print("TOTAL AMT STR IS " + data[total_amt_index][VALUE])
  
  return data[total_amt_index][VALUE]
  # if total_amt_index != 1:
  #   total_cost = data[total_amt_index][VALUE]
  #   if total_cost[0] == "$":
  #     total_cost = total_cost[1:]
  #   total_cost_float = float(total_cost)
  #   return(total_cost_float)