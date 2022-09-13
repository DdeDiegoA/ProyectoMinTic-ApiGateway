from wsgiref import headers
from dotenv import dotenv_values
import requests
config= dotenv_values('.env')

class MesaController():
    def __init__(self):
        pass
    
    def create_mesa(self,data):
        headers= {
            "Content-Type": "application/json"
        }
        response = requests.post(url=f"{config['URL_RESULT']}/mesa/",json=data, headers=headers)
        if response.status_code==201:
            return response.json(),200
        return {
            "message": "Error"
        },400