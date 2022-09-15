from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import dotenv_values
from routes.auth_routes import auth_module
from routes.mesa_routes import mesa_module
from routes.partido_routes import partido_module
from routes.candidato_routes import candidato_module
from routes.resultado_routes import resultado_module
from routes.user_routes import user_module
from routes.role_routes import role_module
from flask_jwt_extended import JWTManager

app = Flask(__name__)
cors=CORS(app)
config=dotenv_values('.env')
jwt=JWTManager(app)

app.register_blueprint(auth_module, url_prefix='/auth')
app.register_blueprint(mesa_module, url_prefix='/mesa')
app.register_blueprint(partido_module, url_prefix='/partido')
app.register_blueprint(candidato_module, url_prefix='/candidato')
app.register_blueprint(resultado_module, url_prefix='/resultado')
app.register_blueprint(user_module, url_prefix='/user')
app.register_blueprint(role_module, url_prefix='/role')
app.config["JWT_SECRET_KEY"]=config['JWT_SECRET']

@app.route('/')
def hello_word():
    dictToReturn = {'message': 'Hola mundirilijillo'}
    return jsonify(dictToReturn)

if __name__ == '__main__':
    app.run(host='localhost', port=config['PORT'], debug=True)