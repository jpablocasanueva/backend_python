from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users_list = [User(name= 'Bruno', surname= 'Casanueva', url= 'https://bruno.casanueva.com', age= 8),
                User(name= 'Luna', surname= 'Casanueva', url= 'https://luna.casanueva.com', age= 9),
                User(name= 'Oso', surname= 'Casanueva', url= 'https://oso.casanueva.com', age= 3)]

@app.get('/usersJson')
async def users():
    return  [{'name': 'Bruno', 'surname': 'Casanueva', 'url':'https://bruno.casanueva.com', 'age': 8},
             {'name': 'Luna', 'surname': 'Casanueva', 'url':'https://luna.casanueva.com', 'age': 9},
             {'name': 'Oso', 'surname': 'Casanueva', 'url':'https://oso.casanueva.com', 'age': 3}]
    
@app.get('/userClass')
async def usersClass():
    return users_list