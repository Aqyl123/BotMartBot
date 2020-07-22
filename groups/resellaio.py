import requests

url = 'https://dev.botmart.io/api/product/resell-aio20373'
response = requests.get(url)
response.raise_for_status()
result = response.json()

name5 = result["data"]["product"]["name"]
picture5 = result["data"]["product"]["thumbnails"]
retail5 = result["data"]["product"]["retail"]
website5 = result["data"]["product"]["website"]
lowestask5 = result["data"]["lowest_ask_renewal"]
description5 = result["data"]["product"]["description"]
twitter5 = result["data"]["product"]["social_media"]["twitter"]
supports5 = result["data"]["product"]["tags"]

url2 = 'https://dev.botmart.io/api/product/3/lowest-ask?require_renewal=False&plan=Lifetime'
response = requests.get(url2)
response.raise_for_status()
result2 = response.json()

lifetime2 = result2["data"]["price"]