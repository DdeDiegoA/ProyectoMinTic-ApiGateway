from urllib import request, response
from flask import Blueprint, jsonify, request
from controllers.partido_controller import PartidoController
from decorators.token_decorator import token, role

partido_module= Blueprint("partido",__name__)
controller= PartidoController()    

@partido_module.post('/create')
@token
@role()
def create():
    response, code = controller.create_partido(request.get_json())
    return jsonify(response),code
      
@partido_module.get('/')
@token
@role()
def get_partido():
    response,code= controller.get_partido(request.args)
    return jsonify(response),code

@partido_module.get('/<string:id>')
@token
@role()
def get_partido_id(id):
    response,code = controller.get_partido_id(request.args,id)
    return jsonify(response),code

@partido_module.put('/<string:id>')
@token
@role()
def upd_partido(id):
    response,code = controller.upd_partido(id,request.get_json())
    return jsonify(response),code

@partido_module.delete('/<string:id>')
@token
@role()
def delete_partido(id):
    response,code = controller.delete_partido(id,request.args)
    return jsonify(response),code