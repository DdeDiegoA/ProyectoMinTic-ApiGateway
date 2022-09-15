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
    return jsonify(response),code
      
@mesa_module.get('/')
@token
@role("Admin")
def get_mesas():
    response,code= controller.get_mesas(request.args)
    return jsonify(response),code

@mesa_module.get('/<string:id>')
@token
@role("Admin")
def get_mesa_id(id):
    response,code = controller.get_mesa_id(request.args,id)
    return jsonify(response),code

@mesa_module.put('/<string:id>')
@token
@role("Admin")
def upd_mesa(id):
    response,code = controller.upd_mesa(id,request.get_json())
    return jsonify(response),code

@mesa_module.delete('/<string:id>')
@token
@role("Admin")
def delete_mesa(id):
    response,code = controller.delete_mesa(id,request.args)
    return jsonify(response),code