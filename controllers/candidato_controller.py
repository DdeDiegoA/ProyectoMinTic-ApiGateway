from urllib import response
from wsgiref import headers
from dotenv import dotenv_values
from flask import Blueprint, jsonify, request
import requests

config= dotenv_values('.env')

class CandidatoController():
    def __init__(self):
        pass
    
    def create_candidato(self,partido_id,data):
        headers= {
            "Content-Type": "application/json"
        }
        response = requests.post(url=f"{config['URL_RESULT']}/candidato/partido/{partido_id}",json=data, headers=headers)
        if response.status_code==201:
            return response.json(),201
        return {
            "message": "Error"
        },400
        
    def get_candidato(self,args):
        headers = {
         "Content-Type": "application/json"
        }
        response= requests.get(url=f"{config['URL_RESULT']}/candidato", headers= headers)
        if response.status_code ==200:
            return response.json(),200
        return response.json()
    
    def get_candidato_id(self,args,id):
        headers = {
         "Content-Type": "application/json"
        }
        response= requests.get(url=f"{config['URL_RESULT']}/candidato/{id}", headers= headers)
        if response.status_code ==200:
            return response.json(),200
        return {
            "messagge":"Id no encotrado"
        }
    
    def upd_candidato(self,id,data):
        headers = {
         "Content-Type": "application/json"
        }
        response= requests.put(url=f"{config['URL_RESULT']}/candidato/{id}", json=data, headers=headers)
        if response.status_code == 204:
            return {},204
        return {
            "messagge":"Id no encontrado"
        },400
        
    def delete_candidato(self,id,args):
        headers = {
         "Content-Type": "application/json"
        }
        response= requests.delete(url=f"{config['URL_RESULT']}/candidato/{id}", headers=headers)
        print(response.status_code)
        if response.status_code == 204:
            return{
                "message":"Eliminacion exitosa B)"
                },204
        return{
            "message":"Id no encontrado"
        },400