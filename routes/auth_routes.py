from urllib import request, response
from flask import Blueprint, jsonify, request
from controllers.auth_controller import AuthController
from decorators.token_decorator import token

auth_module= Blueprint("auth",__name__)
controller= AuthController()

@auth_module.post('/')
def login():
    response, code = controller.login(request.get_json())
    return jsonify(response), code

@auth_module.get('/me')
@token
def me():
    response, code = controller.me(request.args['user_id'])
    return jsonify(response),code