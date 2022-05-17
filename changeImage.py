#!/usr/bin/env python3

import os
import sys
import logging
import requests

from PIL import Image

logger = logging.getLogger(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "supplier-data", "images")

def process_image(image_name):
    new_image_name = image_name.split(".")[0] + ".jpeg"
    image_path = os.path.join(IMAGE_DIR, image_name)
    output_path = os.path.join(IMAGE_DIR, new_image_name)
    img = Image.open(image_path)
    img.rotate(270).resize((600,400)).convert("RGB").save(output_path, "JPEG")
    return output_path

def upload_image(image_name):
    url = "http://130.211.206.58/upload/"
    image_list = os.listdir(IMAGE_DIR)
    with open(image_name, 'rb') as opened:
        r = requests.post(url, files={'file': opened})

if __name__ == "__main__":
    image_list = os.listdir(IMAGE_DIR)
    for img_path in image_list:
        try:
            output_path = process_image(img_path)
            # upload_image(output_path)
        except Exception as err:
            logger.error("ImageError: {}".format(err))
