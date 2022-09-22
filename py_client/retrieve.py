"""Test client that gets a use's details"""
import requests
import authenticate


token = authenticate.authenticate(username='Test3')

if token:
    # id = 'ead783f3-d20b-43ce-80e9-d92d9bc9abf8'
    id = '7b7673b3-183e-4083-a267-95962efb3815'
    # endpoint = f"http://localhost:8000/api/users/4/"
    endpoint = f"http://localhost:8000/api/orders/{id}/"

    get_response = requests.get(endpoint, headers={
                'Authorization': f'Bearer {token}'
                }, )
    print(get_response.headers)
    print(get_response)
    if get_response.status_code in [200, 201]:
        print(get_response.json())