from fastapi import FastAPI, APIRouter, HTTPException, Depends
from schemas import SignupRequest, SigninRequest, TokenResponse
from utils import create_access_token, verify_password, hash_password
from database import database
from models import User
from bson import ObjectId

app = FastAPI()
router = APIRouter()

@router.post("/signup", response_model=TokenResponse, tags=["Auth"])
async def signup(user: SignupRequest):
    """
    Create a new user and return access and refresh tokens.
    """
    user_exists = await database["users"].find_one({"email": user.email})
    if user_exists:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = hash_password(user.password)
    new_user = {
        "name": user.name,
        "email": user.email,
        "password": hashed_password
    }
    await database["users"].insert_one(new_user)

    access_token = create_access_token(data={"email": user.email})
    refresh_token = create_access_token(data={"email": user.email}, expires_delta=30) 

    return {"message": "User created successfully", "access_token": access_token, "refresh_token": refresh_token}

@router.post("/signin", response_model=TokenResponse, tags=["Auth"])
async def signin(user: SigninRequest):
    """
    Sign in an existing user and return access and refresh tokens.

    This endpoint allows a new user to register by providing their name, email, and password.
    If the email is already registered, it returns a 400 status code.
    """
    existing_user = await database["users"].find_one({"email": user.email})
    if not existing_user or not verify_password(user.password, existing_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_access_token(data={"email": user.email})
    refresh_token = create_access_token(data={"email": user.email}, expires_delta=30)  

    return {"message": "Signin successful", "access_token": access_token, "refresh_token": refresh_token}

app.include_router(router)
