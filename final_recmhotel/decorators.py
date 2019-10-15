
# coding: utf-8




from functools import wraps
from flask import session,redirect,url_for

def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('session get username: ',session.get('username'))
        if session.get('username'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))
        
    return wrapper

