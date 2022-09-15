from urllib import request, response
from flask import Blueprint, jsonify, request
from controllers.resultado_controller import ResultadoController
from decorators.token_decorator import token, role

resultado_module= Blueprint("resultado",__name__)
controller= ResultadoController()    

@resultado_module.post('create/mesa/<string:mesa_id>/candidato/<string:candidato_id>/')
@token
@role()
def create(mesa_id,candidato_id):
    response, code = controller.create_resultado(mesa_id,candidato_id,request.get_json())
    return jsonify(response),code
      
@resultado_module.get('/')
@token
@role()
def get_resultado():
    response,code= controller.get_resultado(request.args)
    return jsonify(response),code

@resultado_module.get('/<string:id>')
@token
@role()
def get_resultado_id(id):
    response,code = controller.get_resultado_id(request.args,id)
    return jsonify(response),code

# @resultado_module.put('/<string:id>')
# @token
# @role("Admin")
# def upd_resultado(id):
#     response,code = controller.upd_resultado(id,request.get_json())
#     return jsonify(response),code

@resultado_module.delete('/<string:id>')
@token
@role()
def delete_resultado(id):
    response,code = controller.delete_resultado(id,request.args)
    return jsonify(response),code

@resultado_module.get('/totalMesa')
@token
@role()
def get_total():
    response,code= controller.get_total(request.args)
    return jsonify(response), code

@resultado_module.get('/totalPartido')
@token
@role()
def get_total_partido():
    response,code= controller.get_total_partido(request.args)
    return jsonify(response), code

@resultado_module.get('/totalCandidato/<string:candidato_id>')
@token
@role()
def get_total_candidato(candidato_id):
    response,code= controller.get_total_partido(candidato_id, request.args)
    return jsonify(response), code