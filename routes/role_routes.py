from urllib import request, response
from flask import Blueprint, jsonify, request
from controllers.role_controller import RoleController
from decorators.token_decorator import token, role

role_module= Blueprint("role",__name__)
controller= RoleController()

@role_module.get('/')
@token
@role()
def get_role():
    response,code= controller.get_role(request.args)
    return jsonify(response),code

@role_module.get('/<string:role>')
@token
# @role()
def get_permission_role(role):
    response = controller.get_permission_role(role,request.args)
    return jsonify(response)