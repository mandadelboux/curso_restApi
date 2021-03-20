from flask import Flask, jsonify
from flask_restful import Api
from resourses.hotel import Hoteis, Hotel
from resourses.usuario import User, UserRegistrer, UserLogin, UserLogout
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db' #Pode mudar para outro banco
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Caso não coloque fica travando
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENABLED'] = True

api = Api(app)
jwt = JWTManager(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

@jwt.token_in_blacklist_loader
def verifica_blacklist(token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado():
    return jsonify({'message': 'You heve been logged out.'}), 401 # Converter um dicionário pra Json

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegistrer, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')

if __name__ == '__main__':
    from sql_alchemy import banco # Não quer q o banco Init seja executado quando chamado de outro arquivo
    banco.init_app(app)
    app.run(debug = True) # Apenas no dev
