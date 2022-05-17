#! /usr/bin/env python3
import json
import os
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEXT_DIR = os.path.join(BASE_DIR, "supplier-data/descriptions")

def process_text(text, image_name):
    post = {
        "name": text[0].strip(),
        "weight": text[1].strip().replace(" lbs", ""),
        "description": text[2].strip(),
        "image_name": image_name,
     }
    return post

def post_fruit(data):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post("http://localhost/fruits", data=json.dumps(data), headers=headers)
    print(data)
    print(r.status_code)

def run():
    text_list = os.listdir(TEXT_DIR)
    data = []
    for text in text_list:
        if text.endswith(".txt"):
            with open(os.path.join(TEXT_DIR, text), 'r+') as txt:
               image_name = text.replace(".txt", ".jpeg")
               lines = txt.readlines()
               post_data = process_text(lines, image_name)
               post_fruit(post_data)
               data.append(post_data)
    return data

if __name__ == "__main__":
    run()
