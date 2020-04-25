from flask import Flask, jsonify, request
from flask_restful import Resource, Api 
from flask_jwt import JWT, jwt_required
from security import authenticate, identity


app = Flask(__name__)
api = Api(app)
app.secret_key = "key"

jwt = JWT(app, authenticate, identity)

items = [
    {
        'name': 'Bread',
        'price': 20
    },
    {
        'name': 'Soap',
        'price': 30
    }
]

# GET       /items
# GET       /item/<name>
# POST      /item/<name> {"price":100}
# PUT       /item/<name> {"price" : 123}
# DELETE    /item/<name>
# POST      /auth {"username":"username1", "password": "password1" } 

'''
200 - SUCCESSFUL
201 - CREATED
202 - ACCEPTED
400 - BAD REQUEST
404 - NOT FOUND
'''

class Item(Resource):
    
    def get(self, name):
        item = next(filter(lambda item: item['name'] == name, items), None)
        return {'item': item}, 200 if item else 404
    
    
    def post(self, name):
        if next(filter(lambda item: item['name'] == name, items), None):
           return {'message': f"item with name {name} already exists"}, 400     

        request_data = request.get_json()
        item = {
            'name': name,
            'price': request_data['price']
        }
        items.append(item)
        return item, 201


class ItemList(Resource):

    @jwt_required()
    def get(self):
        return { 'items': items }, 200

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)