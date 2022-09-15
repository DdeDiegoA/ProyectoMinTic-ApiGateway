import datetime
from email import message
import json
from urllib import request, response
from wsgiref import headers
from dotenv import dotenv_values
from flask_jwt_extended import create_access_token
import requests


config = dotenv_values('.env')


class AuthController():
    def __init__(self):
        pass

    def login(self, data):
        exp_time = int(config['JWT_EXPIRATION'])
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(
            url=f"{config['URL_AUTH']}/api/auth/", json=data, headers=headers)
        if response.status_code == 200:
            user = response.json()
            expires = datetime.timedelta(seconds=exp_time)
            access_token = create_access_token(identity=user['id'],
                                               expires_delta=expires,
                                               additional_claims={
                                                   'seudonimo':user['seudonimo'],
                                                   'role': user['role']['name']
                                                                  })
            return {
                "id": user['id'],
                "access_token": access_token
            }, 200
        return {
            "message": "credenciales invalidas",
        }, 401


    def me(self, id):
        headers = {
         "Content-Type": "application/json"
        }
        response = requests.get(url=f"{config['URL_AUTH']}/api/users/{id}", headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json()