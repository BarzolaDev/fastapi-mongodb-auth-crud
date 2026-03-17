from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate
from app.db.mongo import users_collection
from app.core.security import hash_password

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate):
    # Verificar si ya existe
    existing_user = users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail='El usuario ya existe')
    
    # Hash Password
    hashed_password = hash_password(user.password)

    # Guardar en DB
    users_collection.insert_one({
        "email": user.email,
        "password": hashed_password
    })
    #FastApi lo convierte en Json
    return {"message": "User Created"}


