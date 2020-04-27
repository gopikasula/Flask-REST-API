from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    request_parser = reqparse.RequestParser()
    request_parser.add_argument(
        'price',
        required=True,
        type=int,
        help='price field cannot be left blank and should be integer'
    )
    request_parser.add_argument(
        'store_id',
        required=True,
        type=int,
        help='store_id field cannot be left blank and should be integer'
    )

    def get(self, name):
        item = ItemModel.find_item_by_name(name)
        print(item)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_item_by_name(name):
            return {'message': f"item with name {name} already exists"}, 400

        data = Item.request_parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])

        item.save_item_to_db()

        return item.json(), 201

    def put(self, name):
        data = Item.request_parser.parse_args()
        item = ItemModel.find_item_by_name(name)
        if item:
            item.price = data['price']
            item.store_id = data['store_id']
        else:
            item = ItemModel(name, data['price'], data['store_id'])

        item.save_item_to_db()

        return item.json(), 200

    def delete(self, name):
        item = ItemModel.find_item_by_name(name)
        if item:
            item.delete_item_from_db()
        return {"message": f"Item with name {name} deleted"}, 200


class ItemList(Resource):

    @jwt_required()
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}, 200
