from urllib import request
from flask import Blueprint, jsonify, request
from controllers.auth_controller import AuthController

auth_module= Blueprint("auth",__name__)
controller= AuthController()

@auth_module.post('/')
def login():
    response, code = controller.login(request.get_json())
    return jsonify(response), code