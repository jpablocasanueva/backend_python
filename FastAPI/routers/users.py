from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1,name= 'Bruno', surname= 'Casanueva', url= 'https://bruno.casanueva.com', age= 8),
                User(id=2,name= 'Luna', surname= 'Casanueva', url= 'https://luna.casanueva.com', age= 9),
                User(id=3,name= 'Oso', surname= 'Casanueva', url= 'https://oso.casanueva.com', age= 3)]

@router.get('/usersJson')
async def users():
    return  [{'name': 'Bruno', 'surname': 'Casanueva', 'url':'https://bruno.casanueva.com', 'age': 8},
             {'name': 'Luna', 'surname': 'Casanueva', 'url':'https://luna.casanueva.com', 'age': 9},
             {'name': 'Oso', 'surname': 'Casanueva', 'url':'https://oso.casanueva.com', 'age': 3}]
    
@router.get('/userClass')
async def usersClass():
    return users_list

#Path
@router.get('/user/{id}')
async def userId(id: int):
   return search_user(id)
    
#query    
@router.get('/user/')
async def userId(id: int):
    return search_user(id)
    
    
@router.post('/user/',response_model=User,status_code=201)
async def addUser(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail='El usuario ya existe')
        # return {'error':}
    
    users_list.append(user)
    return user

@router.put('/user/')
async def updateUser(user: User):
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    
    if not found:
        return {'error': 'No se ha actualizado el usuario'}
    else:
        return user
    
@router.delete('/user/{id}')
async def deleteUser(id: int):
     found = False
     
     for index, saved_user in enumerate(users_list):
         if saved_user.id  == id:
             del users_list[index]
             found = True
     
     if not found:
         return {'error': 'No se ha eliminado el usuario'}
                

def search_user(id):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {'error':'Usuario no existe'}