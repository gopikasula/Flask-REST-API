from user import User
from werkzeug.security import safe_str_cmp

def authenticate(name, pwd):
    user = User.find_by_username(name)
    if user and safe_str_cmp(user.password, pwd):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.find_by_user_id(user_id)