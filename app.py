from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.item import Item, ItemList
from resources.user import UserRegister
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "key"

api = Api(app)


@app.before_first_request
def create_table():
    db.create_all()


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
500 - INTERNAL SERVER ERROR
'''

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
