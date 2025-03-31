from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1,name= 'Bruno', surname= 'Casanueva', url= 'https://bruno.casanueva.com', age= 8),
                User(id=2,name= 'Luna', surname= 'Casanueva', url= 'https://luna.casanueva.com', age= 9),
                User(id=3,name= 'Oso', surname= 'Casanueva', url= 'https://oso.casanueva.com', age= 3)]

@app.get('/usersJson')
async def users():
    return  [{'name': 'Bruno', 'surname': 'Casanueva', 'url':'https://bruno.casanueva.com', 'age': 8},
             {'name': 'Luna', 'surname': 'Casanueva', 'url':'https://luna.casanueva.com', 'age': 9},
             {'name': 'Oso', 'surname': 'Casanueva', 'url':'https://oso.casanueva.com', 'age': 3}]
    
@app.get('/userClass')
async def usersClass():
    return users_list

#Path
@app.get('/user/{id}')
async def userId(id: int):
   return search_user(id)
    
#query    
@app.get('/user/')
async def userId(id: int):
    return search_user(id)
    
def search_user(id):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {'error':'Usuario no existe'}