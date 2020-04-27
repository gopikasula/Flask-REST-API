from flask_restful import Resource, reqparse
from models.store import StoreModel


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        required=True,
        help='name is required'
    )

    def get(self, name):
        store = StoreModel.find_store_by_name(name)
        if store:
            return store.json(), 200
        return {'message': 'store not found'}, 404

    def post(self, name):
        if StoreModel.find_store_by_name(name):
            return {'message': f'store with name {name} already exits'}, 400

        store = StoreModel(name)
        store.save_store_to_db()

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_store_by_name(name)

        if store:
            store.delete_store_from_db()

        return {'message': 'store deleted successfully'}


class StoreList(Resource):
    def get(self):
        return {
            'stores': [store.json() for store in StoreModel.query.all()]
        }, 200
