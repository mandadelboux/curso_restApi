from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome':'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
    },
    {
        'hotel_id': 'bravo',
        'nome':'Bravo Hotel',
        'estrelas': 4.4,
        'diaria': 380.90,
        'cidade': 'Mogi Mirim'
    },
    {
        'hotel_id': 'charlie',
        'nome':'Charlie Hotel',
        'estrelas': 3.9,
        'diaria': 320.20,
        'cidade': 'Itapira'
    }
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]} # SELECT * FROM hoteis    

class Hotel(Resource):
    # Definindo construtor
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left in blank") #Não pode enviar um Json sem nome
    atributos.add_argument('estrelas', type=float, required=True, help="The field 'estrelas' cannot be left in blank")
    atributos.add_argument('diaria')
    atributos.add_argument('cidade')

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel not found.'}, 404 #Not found
    
    @jwt_required
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message": "Hotel id '{}' already exists.".format(hotel_id)}, 400 #Bad Request

        dados = Hotel.atributos.parse_args()
        hotel = HotelModel(hotel_id, **dados)

        try: 
             hotel.save_hotel()
        except: 
            return {'message': 'An Internal Error Ocurres Trying To Save Hotel.'}, 500 # Internal Server Error
        return hotel.json()   
    
#Atualizar os dados
    @jwt_required
    def put(self, hotel_id):

        dados = Hotel.atributos.parse_args()
        hotel_encontrado = HotelModel.find_hotel(hotel_id)

        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(),200 # Ok
        hotel = HotelModel(hotel_id, **dados)

        try: 
             hotel.save_hotel()
        except: 
            return {'message': 'An Internal Error Ocurres Trying To Save Hotel.'}, 500 # Internal Server Error
        return hotel.json(), 201 # Created
        
    @jwt_required
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'An Error Ocurred Trying To Delete Hotel'}, 500 
            return { 'message': 'Hotel deleted.'}
        return { 'message': 'Hotel not found.'}, 404

