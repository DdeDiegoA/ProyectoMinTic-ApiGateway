from urllib import response
from wsgiref import headers
from dotenv import dotenv_values
from flask import Blueprint, jsonify, request
import requests
config= dotenv_values('.env')

class RoleController():
    def __init__(self):
        pass
    
    def get_role(self,args):
        headers = {
         "Content-Type": "application/json"
        }
        response = requests.get(url=f"{config['URL_AUTH']}/api/roles/", headers=headers)
        if response.status_code ==200:
            return response.json(),200
        return response.jsrole
    
    def get_permission_role(self,role,args):
        headers = {
         "Content-Type": "application/json"
        }
        response = requests.get(url=f"{config['URL_AUTH']}/api/roles/{role}", headers= headers)
        if response.status_code ==200:
            return response.json(),200
        return {
            "messagge":"Id no encotrado"
        }