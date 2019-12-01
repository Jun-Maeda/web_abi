import requests

zip = input('郵便番号を入力してください。')

response = requests.get(f'http://zipcloud.ibsnet.co.jp/api/search?zipcode={zip}')
zip_json = response.json()
zip_address = zip_json['results'][0]
都道府県 = zip_address['address1']
市町村 = zip_address['address2']
地域 = zip_address['address3']
address = f'{都道府県}{市町村}{地域}'
print(address)


