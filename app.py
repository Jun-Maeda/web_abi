import requests

response = requests.get('http://zipcloud.ibsnet.co.jp/api/search?zipcode=7830060')
print(response.text)