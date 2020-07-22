import requests

url = 'https://dev.botmart.io/api/product/fleek14065'
response = requests.get(url)
response.raise_for_status()
result = response.json()

name = result["data"]["product"]["name"]
picture = result["data"]["product"]["thumbnails"]
retail = result["data"]["product"]["retail"]
website = result["data"]["product"]["website"]
lowestask = result["data"]["lowest_ask_renewal"]
description = result["data"]["product"]["description"]
twitter = result["data"]["product"]["social_media"]["twitter"]
supports = result["data"]["product"]["tags"][0]

url2 = 'https://dev.botmart.io/api/product/7/lowest-ask?require_renewal=False&plan=Lifetime'
response = requests.get(url2)
response.raise_for_status()
result2 = response.json()

lifetime = result2["data"]["price"]