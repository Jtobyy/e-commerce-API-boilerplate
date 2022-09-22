"""Test client that gets a users"""
import requests
import authenticate


token = authenticate.authenticate(username='Test3')

if token:
    headers = {
        "Authorization": f'Bearer {token}'
    }

    user_id = 1
    # endpoint = "http://localhost:8000/api/users/"
    # endpoint = "http://localhost:8000/api/products/"
    endpoint = "http://localhost:8000/api/orders/"

    get_response = requests.get(endpoint, headers=headers)    
    print(get_response.headers)
    print(get_response.json())
