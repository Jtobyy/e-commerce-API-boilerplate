import requests

# Intialize a basic endpoint
# endpoint = 'http://localhost:8000/api/users/register/'

# data = {
#     'first_name': 'Test4',
#     'last_name': 'Test4',
#     'username': 'Test4',
#     'email': 'test1@gmail.com',
#     'password': 'test2022',
#     'address': 'test street',
#     'city': 'test city',
#     'state': 'test state',
#     'country': 'test country',
# }

import authenticate


token = authenticate.authenticate(username='admin')

if token:
    endpoint = 'http://localhost:8000/api/products/3'

    # Maker request to the endpoint and print out the respons
    response = requests.delete(endpoint, headers={
        'Authorization': f'Bearer {token}'
    })
    print(response)
    print(response.text)
    print(response.status_code)