from urllib import response
from wsgiref import headers
from dotenv import dotenv_values
from flask import Blueprint, jsonify, request
import requests

config= dotenv_values('.env')

class UserController():
    def __init__(self):
        pass
    
    def create_user(self,data):
        headers= {
            "Content-Type": "application/json"
        }
        response = requests.post(url=f"{config['URL_AUTH']}/api/users/", json=data,headers=headers)
        if response.status_code==200:
            return response.json(),201
        return {
            "message": "Error"
        },400
        
    def get_user(self,args):
        headers = {
         "Content-Type": "application/json"
        }
        response = requests.get(url=f"{config['URL_AUTH']}/api/users/", headers=headers)
        if response.status_code ==200:
            return response.json(),200
        return response.json()
    
    def get_user_id(self,args,id):
        headers = {
         "Content-Type": "application/json"
        }
        response = requests.get(url=f"{config['URL_AUTH']}/api/users/id/{id}", headers= headers)
        if response.status_code ==200:
            return response.json(),200
        return {
            "messagge":"Id no encotrado"
        }
        
    def get_user_role(self,args,role):
        headers = {
         "Content-Type": "application/json"
        }
        response = requests.get(url=f"{config['URL_AUTH']}/api/users/roles/{role}", headers= headers)
        if response.status_code ==200:
            return response.json(),200
        return {
            "messagge":"Id no encotrado"
        }
    
    def upd_user(self,id,data):
        headers = {
         "Content-Type": "application/json"
        }
        response = requests.put(url=f"{config['URL_AUTH']}/api/users/{id}", json=data, headers=headers)
        if response.status_code == 204:
            return {},204
        return {
            "messagge":"Id no encontrado"
        },400
        
    def delete_user(self,id,args):
        headers = {
         "Content-Type": "application/json"
        }
        response = requests.delete(url=f"{config['URL_AUTH']}/api/users/{id}", headers=headers)
        print(response.status_code)
        if response.status_code == 204:
            return{
                "message":"Eliminacion exitosa B)"
                },204
        return{
            "message":"Id no encontrado"
        },400