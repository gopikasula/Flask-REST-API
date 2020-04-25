from user import User
from werkzeug.security import safe_str_cmp


users = [
    User(1, 'username1', 'password1'),
    User(2, 'username2', 'password2')   
]


username_map = { user.username : user for user in users }
user_id_map = { user.id : user for user in users }


def authenticate(name, pwd):
    user = username_map.get(name, None)
    if user and safe_str_cmp(user.password, pwd):
        return user


def identity(payload):
    user_id = payload['identity']
    return user_id_map.get(user_id, None)