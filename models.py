from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    name: str
    email: str
    password: str  

class Organization(BaseModel):
    name: str
    description: Optional[str] = None

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class OrganizationResponse(BaseModel):
    organization_id: str
    name: str
    description: Optional[str]
    organization_members: List[dict]  
