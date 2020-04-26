from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

class Item(Resource):
   
   
    request_parser = reqparse.RequestParser()
    request_parser.add_argument(
        'price',
        required= True,
        type= int,
        help = 'price field cannot be left blank and should be integer'
    )

    @classmethod
    def find_item_by_name(cls, name):
        connection = sqlite3.connect('item.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name =?"
        item = cursor.execute(query, (name, )).fetchone()        
        
        if item:
            return {'name': item[0],'price': item[1]}
    
    @classmethod
    def insert_item(cls, item):
        
        connection = sqlite3.connect('item.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES(?, ?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()

    @classmethod
    def update_item(cls, item):
        
        connection = sqlite3.connect('item.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? where name=?"
        cursor.execute(query, (item['price'], item['name']))

        connection.commit()
        connection.close()

    def get(self, name):
        item = Item.find_item_by_name(name)
        if item:
            return item
        return {'message': 'Item not found'}, 404    
        
    
    def post(self, name):
        if Item.find_item_by_name(name):
           return {'message': f"item with name {name} already exists"}, 400     
        
        data = Item.request_parser.parse_args()
        item = {
            'name': name,
            'price': data['price']
        }
        try:
            Item.insert_item(item)
        except:
            return {'message': 'Error occured while inserting item'}, 500

        return item, 201


    def put(self, name):
        data = Item.request_parser.parse_args()
        update_item = {
            'name': name,
            'price': data['price']
        }
        item = Item.find_item_by_name(name)
        if item:
            try:
                Item.update_item(update_item)
            except Exception as ex:
                print(ex)
                return {'message': 'Error occured while updating item'}, 500 
            return update_item, 200
        else:
            try:
                Item.insert_item(update_item)
            except:
                return {'message': 'Error occured while inserting item'}, 500 
            return update_item, 200


    def delete(self, name):
        
        connection = sqlite3.connect('item.db')
        cursor = connection.cursor()

        query = "DELETE FROM items where name=?"
        cursor.execute(query, (name, ))       
        
        connection.commit()
        connection.close()

        return {"message" : f"Item with name {name} deleted"}, 200


class ItemList(Resource):

    @jwt_required()
    def get(self):
        connection = sqlite3.connect('item.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM items"
        rows = cursor.execute(query)
        items = []
        
        for row in rows:
            items.append({'name': row[0], 'price': row[1]})

        connection.close()

        return { 'items': items }, 200