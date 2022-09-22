import requests

# Intialize a basic endpoint
# endpoint = 'http://localhost:8000/api/users/register/'

data = {
    'first_name': 'Test4',
    'last_name': 'Test4',
    'username': 'Test4',
    'email': 'test1@gmail.com',
    'password': 'test2022',
    'address': 'test street',
    'city': 'test city',
    'state': 'test state',
    'country': 'test country',
}

endpoint = 'http://localhost:8000/api/users//'
response = requests.post(endpoint, data=data)

# import authenticate


# token = authenticate.authenticate(username='Test3')

# if token:
#     # endpoint = 'http://localhost:8000/api/products/'


#     # # Make request to the endpoint and print out the respons
#     # data = {
#     #     'id': '3',
#     #     'name': 'Test product 3',
#     #     'description': 'lacks description',
#     #     'regular_price': '24000',
#     #     'sale_price': '40000',
#     #     'weight': '40',
#     #     'inventory': '1000',
#     # # }
#     # endpoint = 'http://localhost:8000/api/orders/'
#     endpoint = 'http://localhost:8000/api/payments/'


#     # Make request to the endpoint and print out the respons
#     # data = {
#     #     'name': 'Test product 2',
#     #     'product': '2',
#     #     'amount': '3',
#     #     'price_paid': '40000',
#     # }
#     # data = {
#     #     'order': '263bf875-e579-4949-857d-0dee0fcaefc6',
#     #     'amount': '3000',
#     #     'status': 'P',
#     # }
#     data = {
#         'order': '240cd832-d281-4edd-8916-85ca2d400272',
#         'amount': '3000',
#         'status': 'P',
#     }
    
    

#     response = requests.post(endpoint, data=data, headers={
#         'Authorization': f'Bearer {token}'
#     })
#     print(response)
#     print(response.text)
#     print(response.status_code)