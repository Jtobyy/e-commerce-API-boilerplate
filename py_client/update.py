import requests
import authenticate


token = authenticate.authenticate(username='Test1')

if token:
    user_id = input('user id: ')    
    # Intialize a basic endpoint
    # endpoint = f"http://localhost:8000/api/users/{user_id}/"
    endpoint = f"http://localhost:8000/api/products/{user_id}/"

    response = requests.patch(endpoint, headers={
                'Authorization': f'Bearer {token}'
                }, 
                data={'name': 'Test product 1 edit 1'})
    # response = requests.put(endpoint, data={...})

    print(response.text)
