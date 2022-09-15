from urllib import response
from wsgiref import headers
from dotenv import dotenv_values
from flask import Blueprint, jsonify, request
import requests

config= dotenv_values('.env')

class PartidoController():
    def __init__(self):
        pass
    
    def create_partido(self,data):
        headers= {
            "Content-Type": "application/json"
        }
        response = requests.post(url=f"{config['URL_RESULT']}/partido",json=data, headers=headers)
        if response.status_code==201:
            return response.json(),201
        return {
            "message": "Error"
        },400
        
    def get_partido(self,args):
        headers = {
         "Content-Type": "application/json"
        }
        response= requests.get(url=f"{config['URL_RESULT']}/partido", headers= headers)
        if response.status_code ==200:
            return response.json(),200
        return response.json()
    
    def get_partido_id(self,args,id):
        headers = {
         "Content-Type": "application/json"
        }
        response= requests.get(url=f"{config['URL_RESULT']}/partido/{id}", headers= headers)
        if response.status_code ==200:
            return response.json(),200
        return {
            "messagge":"Id no encotrado"
        }
    
    def upd_partido(self,id,data):
        headers = {
         "Content-Type": "application/json"
        }
        response= requests.put(url=f"{config['URL_RESULT']}/partido/{id}", json=data, headers=headers)
        if response.status_code == 204:
            return {},204
        return {
            "messagge":"Id no encontrado"
        },400
        
    def delete_partido(self,id,args):
        headers = {
         "Content-Type": "application/json"
        }
        response= requests.delete(url=f"{config['URL_RESULT']}/partido/{id}", headers=headers)
        print(response.status_code)
        if response.status_code == 204:
            return{
                "message":"Eliminacion exitosa B)"
                },204
        return{
            "message":"Id no encontrado"
        },400