import requests

url = 'https://dev.botmart.io/api/product/estocksoftware25107'
response = requests.get(url)
response.raise_for_status()
result = response.json()

nameESTOCK = result['data']['product']['name']
pictureESTOCK = result['data']['product']['thumbnails']
retailESTOCK = result['data']['product']['retail']
websiteESTOCK = result['data']['product']['website']
lowestaskESTOCK = result['data']['lowest_ask_renewal']
descriptionESTOCK = result['data']['product']['description']
twitterESTOCK = result['data']['product']['social_media']['twitter']
supportsESTOCK = result['data']['product']['tags']