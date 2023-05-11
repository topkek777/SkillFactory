import json
import requests

url = 'https://petstore.swagger.io/v2'

res_get = requests.get(f'{url}/pet/findByStatus', params={'status': 'available'},
                       headers={'accept': 'application/json'})
print(f'Код запроса get = {res_get.status_code}')

data_post = {
    'name': 'bro',
    'photoUrls': [
        'string'
    ]
}
res_post = requests.post(f'{url}/pet',
                         headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                         data=json.dumps(data_post))
print(f'Код запроса post = {res_post.status_code}')

petId = res_post.json()['id']
res_delete = requests.delete(f'{url}/pet/{petId}', headers={'accept': 'application/json'})
print(f'Код запроса delete = {res_delete.status_code}')

data_put = {
    'name': 'brother',
}
res_put = requests.put(f'{url}/pet', \
                       headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                       data=json.dumps(data_put)
                       )
print(f'Код запроса put = {res_put.status_code}')
