from fastapi import FastAPI
from shcemas import Item
users_db = [
    {
        'user_id': 1,
        'name': 'Alice',
        'subscription': 'free tier'
    },
    {
        'user_id': 2,
        'name': 'Bob',
        'subscription': 'premium tier'
    },
    {
        'user_id': 3,
        'name': 'Clementine',
        'subscription': 'free tier'
    }
]
api = FastAPI()
@api.get('/')
def get_index():
    return {
        'greetings': 'welcome'
    }
# http://127.0.0.1:8000/users
# [{"user_id":1,"name":"Alice","subscription":"free tier"},
#  {"user_id":2,"name":"Bob","subscription":"premium tier"},
#  {"user_id":3,"name":"Clementine","subscription":"free tier"}]
@api.get('/users')
def get_users():
    return users_db
@api.get('/users/{userid:int}')
def get_user(userid):
    try:
        user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]
        return user
    except IndexError:
        return {}
@api.get('/users/{userid:int}/name')
def get_user_name(userid):
    try:
        user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]
        return {'name': user['name']}
    except IndexError:
        return {}
@api.get('/users/{userid:int}/subscription')
def get_user_suscription(userid):
    try:
        user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]
        return {'subscription': user['subscription']}
    except IndexError:
        return {}

@api.post('/item')
def post_item(item: Item):
    return {
        'itemid': item.itemid
    }

# uvicorn app_exercise:api --reload
