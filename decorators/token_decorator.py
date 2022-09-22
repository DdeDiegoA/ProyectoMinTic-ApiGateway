from functools import wraps
from importlib.resources import contents
from flask import request,jsonify
from flask_jwt_extended import decode_token
from dotenv import dotenv_values
from werkzeug.datastructures import ImmutableMultiDict
import traceback
import requests

config = dotenv_values('.env')
def token(f):
  """
  It takes a function as an argument, and returns a function that takes the same arguments as the
  original function, and returns the same thing as the original function, but only after doing some
  stuff first
  
  :param f: The function that is being decorated
  :return: The function decorated is being returned.
  """
  @wraps(f)
  def decorated(*args,**kwargs):
        token= request.headers.get('Authorization','no hay token')
        parts= token.split()
        if parts[0] != 'Bearer':
            return jsonify({
                'message': 'Token mal formateado'
            }),401
        decoded= decode_token(parts[1])
        http_args= request.args.to_dict()
        http_args['user_id']= decoded['sub']
        http_args['role']= decoded['role']
        request.args= ImmutableMultiDict(http_args)
        return f(*args,**kwargs)
  return decorated

def role():
  """
  It takes a function as an argument, and returns a function that takes a function as an argument, and
  returns a function that takes a function as an argument, and returns a function that takes a
  function as an argument, and returns a function that takes a function as an argument, and returns a
  function that takes a function as an argument, and returns a function that takes a function as an
  argument, and returns a function that takes a function as an argument, and returns a function that
  takes a function as an argument, and returns a function that takes a function as an argument, and
  returns a function that takes a function as an argument, and returns a function that takes a
  function as an argument, and returns a function that takes a function as an argument, and returns a
  function that takes a function as an argument, and returns a function that takes a function as an
  argument, and returns a function that takes a function as an argument, and returns a function that
  takes a function as an
  :return: A function that returns a function that returns a function.
  """
  def inner_decorator(f):
    @wraps(f)
    def decorated(*args, **kwargs):
      try:
        headers = {
          "Content-Type": "application/json"
        }
        token= request.headers.get('Authorization','no hay token')
        parts= token.split()
        decoded= decode_token(parts[1])
        http_args= request.args.to_dict()
        http_args['role']= decoded['role']
        response = requests.get(f"{config['URL_AUTH']}/api/roles/{http_args['role']}", headers=headers)
        if response.status_code == 200:
          permission = response.json()
          flag = False
          method = request.method.lower()
          url = request.path
          for p in permission:
            if p['method'].lower() == method and p['url'] in url:
              flag = True
              break
          if flag:
            result = f(*args, **kwargs)
            return result
          return jsonify({
          "message": "No tiene permisos 1"
          }), 403
      except:
        return jsonify({
          "message": "No tiene permisos 2"
        }), 403
    return decorated
  return inner_decorator
      