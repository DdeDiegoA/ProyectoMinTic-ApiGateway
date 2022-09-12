import imp
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import dotenv_values
from routes.auth_routes import auth_module
from flask_jwt_extended import JWTManager

app = Flask(__name__)
cors=CORS(app)
config=dotenv_values('.env')
jwt=JWTManager(app)

app.register_blueprint(auth_module, url_prefix='/auth')
app.config["JWT_SECRET_KEY"]=config['JWT_SECRET']

@app.route('/')
def hello_word():
    dictToReturn = {'message': 'Hola mundirilijillo'}
    return jsonify(dictToReturn)

if __name__ == '__main__':
    app.run(host='localhost', port=config['PORT'], debug=True)