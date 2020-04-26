import sqlite3
from flask_restful import Resource, reqparse

class User():
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_user_id(cls, user_id):
        connection = sqlite3.connect('item.db')
        cursor = connection.cursor()    
        query = "SELECT * FROM users WHERE id=?" 
        row = cursor.execute(query, (user_id, )).fetchone()
        if(row):
            user =  cls(*row)
        else:
            user = None    
        connection.close()
        return user
        

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('item.db')
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username=?"
        row = cursor.execute(query, (username, )).fetchone()
        if(row): 
            user =  cls(*row)
        else:
            user = None    
        connection.close()
        return user

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        required= True,
        help= 'username is a requuired field'
    )
    parser.add_argument(
        'password',
        required= True,
        help= 'password is a required field'
    )

    def post(self):
        data = UserRegister.parser.parse_args()  
        
        user = User.find_by_username(data['username'])
        if user:
            return {'message': 'User with provided username already exits'}, 400

        connection = sqlite3.connect('item.db')
        cursor = connection.cursor()
        
        insert_query = "INSERT INTO users VALUES(NULL, ?, ?)"
        cursor.execute(insert_query, (data['username'], data['password']))
        
        connection.commit()
        connection.close()
        
        return {'message': 'User created successfully'}, 201

