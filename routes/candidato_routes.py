from urllib import request, response
from flask import Blueprint, jsonify, request
from controllers.candidato_controller import CandidatoController
from decorators.token_decorator import token, role

candidato_module= Blueprint("candidato",__name__)
controller= CandidatoController()    

@candidato_module.post('create/partido/<string:partido_id>/')
@token
@role("Admin")
def create(partido_id):
    response, code = controller.create_candidato(partido_id,request.get_json())
    return jsonify(response),code
      
@candidato_module.get('/')
@token
@role("Admin")
def get_candidato():
    response,code= controller.get_candidato(request.args)
    return jsonify(response),code

@candidato_module.get('/<string:id>')
@token
@role("Admin")
def get_candidato_id(id):
    response,code = controller.get_candidato_id(request.args,id)
    return jsonify(response),code

@candidato_module.put('/<string:id>')
@token
@role("Admin")
def upd_candidato(id):
    response,code = controller.upd_candidato(id,request.get_json())
    return jsonify(response),code

@candidato_module.delete('/<string:id>')
@token
@role("Admin")
def delete_candidato(id):
    response,code = controller.delete_candidato(id,request.args)
    return jsonify(response),code