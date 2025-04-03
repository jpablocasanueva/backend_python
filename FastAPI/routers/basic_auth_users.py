from fastapi import FastAPI, Depends, HTTPException,status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    usernname: str
    full_name: str
    email: str
    disabled: bool
    
class UserDB(User):
    password: str
    
users_db ={
    "guasonico":{
        "usernname": "guasonico",
        "full_name": "Jose Casanueva",
        "email": "guasonico@wenei.cl",
        "disabled": False,
        "password": "123456"
    },
    "bruno2015":{
        "usernname": "bruno2015",
        "full_name": "Bruce Wayne",
        "email": "bruce@wenei.cl",
        "disabled": True,
        "password": "654321"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Credenciales de autenticacion invalidas",
                            headers={"WWW-Authenticate": "Beaver"})
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Usuario Inactivo")
    return user
    
@app.post('/login')
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Usuario no es correcto")
    
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contrasena no es correcta")
    
    return {"access_token": user.usernname, "token_type": "bearer"}
    
@app.get('/users/me')
async def me(user: User = Depends(current_user)):
    return user
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
