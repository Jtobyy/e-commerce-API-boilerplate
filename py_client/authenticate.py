"""Test client that gets a users"""
import requests
from getpass import getpass


def authenticate(username):
    auth_endpoint = "http://localhost:8000/api/auth/"
    password = getpass()
    auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
    if auth_response.status_code == 200:
        print(auth_response.json())
        return auth_response.json()['token']
    else:
        print(auth_response, auth_response.status_code, auth_response.text)

