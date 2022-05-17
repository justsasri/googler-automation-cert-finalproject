#!/usr/bin/env python3

import os
import sys
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "supplier-data", "images")

def upload_image(image_name):
    url = "http://130.211.206.58/upload/"
    image_list = os.listdir(IMAGE_DIR)
    with open(image_name, 'rb') as opened:
        r = requests.post(url, files={'file': opened})

if __name__ == "__main__":
    image_list = os.listdir(IMAGE_DIR)
    for img in image_list:
       if img.endswith(".jpeg"):
          upload_image(os.path.join(IMAGE_DIR, img))
          print(os.path.join(IMAGE_DIR, img))
       else:
          continue

