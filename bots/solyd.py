import requests

url = 'https://dev.botmart.io/api/product/solydbot86770'
response = requests.get(url)
response.raise_for_status()
result = response.json()

nameSOLYD = result['data']['product']['name']
pictureSOLYD = result['data']['product']['thumbnails']
websiteSOLYD = result['data']['product']['website']
descriptionSOLYD = result['data']['product']['description']
twitterSOLYD = result['data']['product']['social_media']['twitter']
supportsSOLYD = result['data']['product']['tags']

# # LIFETIME PRICING
# urlLTSOLYD = 'https://dev.botmart.io/api/product/12/lowest-ask?require_renewal=False&plan=Lifetime'
# response = requests.get(urlLTSOLYD)
# response.raise_for_status()
# resultLT = response.json()

# lifetimeSOLYD = resultLT['data']['price']

# # RENEWAL 3M PRICING
# url3MSOLYD = 'https://dev.botmart.io/api/product/12/lowest-ask?require_renewal=True&plan=Renewal%203M'
# response = requests.get(url3MSOLYD)
# response.raise_for_status()
# result3M = response.json()

# renewal3MSOLYD = result3M['data']['price']

# RENEWAL 6M PRICING
url6MSOLYD = 'https://dev.botmart.io/api/product/12/lowest-ask?require_renewal=True&plan=Renewal%206M'
response = requests.get(url6MSOLYD)
response.raise_for_status()
result6M = response.json()

renewal6MSOLYD = result6M['data']['price']