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
        """
        It receives a json with the user's credentials, it sends a request to the authentication service,
        if the response is 200, it creates a token with the user's id, the expiration time and the user's
        role, and returns the token and the user's id
        
        :param data: {
        :return: A dictionary with the id and access_token
        """
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
        """
        It takes in an id, makes a request to the auth service, and returns the response
        
        :param id: the id of the user
        """
        headers = {
         "Content-Type": "application/json"
        }
        response = requests.get(url=f"{config['URL_AUTH']}/api/users/id/{id}", headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json()