from urllib import request, response
from flask import Blueprint, jsonify, request
from controllers.mesa_controller import MesaController
from decorators.token_decorator import token, role

mesa_module= Blueprint("mesa",__name__)
controller= MesaController()    

@mesa_module.post('/create')
@token
@role("Admin")
def create():
    response, code = controller.create_mesa(request.get_json())
    return jsonify(response), code

@mesa_module.get('/me')
@token
def me():
    response, code = controller.me(request.args['user_id'])
    return jsonify(response),code       