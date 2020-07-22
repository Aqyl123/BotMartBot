import requests

url = 'https://dev.botmart.io/api/product/thenorthcop67022'
response = requests.get(url)
response.raise_for_status()
result = response.json()

name4 = result["data"]["product"]["name"]
picture4 = result["data"]["product"]["thumbnails"]
retail4 = result["data"]["product"]["retail"]
website4 = result["data"]["product"]["website"]
lowestask4 = result["data"]["lowest_ask_renewal"]
description4 = result["data"]["product"]["description"]
twitter4 = result["data"]["product"]["social_media"]["twitter"]
supports4 = result["data"]["product"]["tags"][0] + ' | ' + result["data"]["product"]["tags"][1]