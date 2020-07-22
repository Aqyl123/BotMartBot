import requests

url = 'https://dev.botmart.io/api/product/cookology04688'
response = requests.get(url)
response.raise_for_status()
result = response.json()

name2 = result["data"]["product"]["name"]
picture2 = result["data"]["product"]["thumbnails"]
retail2 = result["data"]["product"]["retail"]
website2 = result["data"]["product"]["website"]
lowestask2 = result["data"]["lowest_ask_renewal"]
description2 = result["data"]["product"]["description"]
twitter2 = result["data"]["product"]["social_media"]["twitter"]
supports2 = result["data"]["product"]["tags"]