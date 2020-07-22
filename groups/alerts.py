import requests

url = 'https://dev.botmart.io/api/product/alerts86061'
response = requests.get(url)
response.raise_for_status()
result = response.json()

name3 = result["data"]["product"]["name"]
picture3 = result["data"]["product"]["thumbnails"]
retail3 = result["data"]["product"]["retail"]
website3 = result["data"]["product"]["website"]
lowestask3 = result["data"]["lowest_ask_renewal"]
description3 = result["data"]["product"]["description"]
twitter3 = result["data"]["product"]["social_media"]["twitter"]
supports3 = result["data"]["product"]["tags"]