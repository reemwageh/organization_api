from pydantic import BaseModel, EmailStr
from typing import List, Optional

class User(BaseModel):
    name: str
    email: EmailStr
    access_level: str

class OrganizationCreate(BaseModel):
    name: str
    description: str

class OrganizationRead(OrganizationCreate):
    organization_id: str
    organization_members: List[User] = []

class UserInvite(BaseModel):
    user_email: EmailStr

class SignupRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class SigninRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    message: str
