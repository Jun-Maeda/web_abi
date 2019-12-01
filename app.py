import requests

zip = input('郵便番号を入力してください。')

response = requests.get(f'http://zipcloud.ibsnet.co.jp/api/search?zipcode={zip}')
print(response.text)

