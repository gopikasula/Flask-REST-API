from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse 
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from item import Item, ItemList
from user import UserRegister

app = Flask(__name__)
api = Api(app)
app.secret_key = "key"

jwt = JWT(app, authenticate, identity)

# GET       /items
# GET       /item/<name>
# POST      /item/<name> {"price":100}
# PUT       /item/<name> {"price" : 123}
# DELETE    /item/<name>
# POST      /auth {"username":"username1", "password": "password1" } 
# POST      /register {"username":"username1", "password": "password1" } 

'''
200 - SUCCESSFUL
201 - CREATED
202 - ACCEPTED
400 - BAD REQUEST
401 - UNAUTHORIZED
404 - NOT FOUND
'''

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)