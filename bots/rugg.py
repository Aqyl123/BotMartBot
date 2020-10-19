import requests

url = 'https://dev.botmart.io/api/product/ruggaio-bot80355'
response = requests.get(url)
response.raise_for_status()
result = response.json()

nameRUGG= result['data']['product']['name']
pictureRUGG = result['data']['product']['thumbnails']
websiteRUGG = result['data']['product']['website']
descriptionRUGG = result['data']['product']['description']
twitterRUGG = result['data']['product']['social_media']['twitter']
supportsRUGG = result['data']['product']['tags']

urlRENEWAL2 = 'https://dev.botmart.io/api/product/22/lowest-ask?require_renewal=True&plan=RENEWAL2'
response = requests.get(urlRENEWAL2)
response.raise_for_status()
resultRENEWAL2 = response.json()

renewal2 = resultRENEWAL2['data']['price']

urlLIFETIME = 'https://dev.botmart.io/api/product/22/lowest-ask?require_renewal=False&plan=Lifetime'
response = requests.get(urlLIFETIME)
response.raise_for_status()
resultLIFETIME = response.json()

lifetimeRUGG = resultLIFETIME['data']['price']

urlRENEWAL = 'https://dev.botmart.io/api/product/22/lowest-ask?require_renewal=True&plan=RENEWAL'
response = requests.get(urlRENEWAL)
response.raise_for_status()
resultRENEWAL = response.json()

renewalRUGG = resultRENEWAL['data']['price']