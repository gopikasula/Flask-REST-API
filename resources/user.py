from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        required=True,
        help='username is a requuired field'
    )
    parser.add_argument(
        'password',
        required=True,
        help='password is a required field'
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        user = UserModel.find_by_username(data['username'])
        if user:
            return {'message': 'Provided username already exits'}, 400

        user = UserModel(data['username'], data['password'])
        user.save_user_to_db()
        return {'message': 'User created successfully'}, 201
