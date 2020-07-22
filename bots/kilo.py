import requests

url = 'https://dev.botmart.io/api/product/kilo11635'
response = requests.get(url)
response.raise_for_status()
result5 = response.json()

name1 = result5["data"]["product"]["name"]
picture1 = result5["data"]["product"]["thumbnails"]
retail1 = result5["data"]["product"]["retail"]
website1 = result5["data"]["product"]["website"]
lowestask1 = result5["data"]["lowest_ask_renewal"]
description1 = result5["data"]["product"]["description"]
twitter1 = result5["data"]["product"]["social_media"]["twitter"]
supports1 = result5["data"]["product"]["tags"]
