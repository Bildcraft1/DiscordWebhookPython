import json
import os
import sys
import requests

print("Input title: ")
title = input()
print("Input desc: ")
desc = input()
print("Input url: ")
url = input()
print("Input imgurl: ")
imgurl = input()

url = "<Input webhook>"
filename = 'request.json'

with open(filename, 'r') as f:
    data = json.load(f)
    data['embeds'][0]['title'] = title
    data['embeds'][0]['description'] = desc
    data['embeds'][0]['url'] = url
    data['embeds'][0]['image']['url'] = imgurl

os.remove(filename)
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)

with open(filename, 'r') as f:
    data = json.load(f)
    x = requests.post(url, json=data)
