from urllib import response
from wsgiref import headers
from dotenv import dotenv_values
from flask import Blueprint, jsonify, request
import requests

config= dotenv_values('.env')

class ResultadoController():
    def __init__(self):
        pass
    
    def create_resultado(self,mesa_id,candidato_id,data):
        headers= {
            "Content-Type": "application/json"
        }
        response = requests.post(url=f"{config['URL_RESULT']}/resultado/mesa/{mesa_id}/candidato/{candidato_id}",json=data, headers=headers)
        if response.status_code==201:
            return response.json(),201
        return {
            "message": "Error"
        },400
        
    def get_resultado(self,args):
        headers = {
         "Content-Type": "application/json"
        }
        response= requests.get(url=f"{config['URL_RESULT']}/resultado", headers= headers)
        if response.status_code ==200:
            return response.json(),200
        return response.json()
    
    def get_resultado_id(self,args,id):
        headers = {
         "Content-Type": "application/json"
        }
        response= requests.get(url=f"{config['URL_RESULT']}/resultado/{id}", headers= headers)
        if response.status_code ==200:
            return response.json(),200
        return {
            "messagge":"Id no encotrado"
        }
    
    # def upd_resultado(self,id,data):
    #     headers = {
    #      "Content-Type": "application/json"
    #     }
    #     response= requests.put(url=f"{config['URL_RESULT']}/candidato/{id}", json=data, headers=headers)
    #     if response.status_code == 204:
    #         return {},204
    #     return {
    #         "messagge":"Id no encontrado"
    #     },400
        
    def delete_resultado(self,id,args):
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
        
    def get_total(self,args):
        headers = {
         "Content-Type": "application/json"
        }
        response= requests.get(url=f"{config['URL_RESULT']}/resultado/total", headers= headers)
        if response.status_code ==200:
            return response.json(),200
        return response.json()
    
    def get_total_partido(self,args):
        headers = {
         "Content-Type": "application/json"
        }
        response= requests.get(url=f"{config['URL_RESULT']}/resultado/totalPartido", headers= headers)
        if response.status_code ==200:
            return response.json(),200
        return response.json()
    
    def get_total_candidato(self,candidato_id,args):
        headers = {
         "Content-Type": "application/json"
        }
        response= requests.get(url=f"{config['URL_RESULT']}/resultado/totalCandidato/{candidato_id}", headers= headers)
        if response.status_code ==200:
            return response.json(),200
        return response.json()
    