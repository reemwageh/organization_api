from motor.motor_asyncio import AsyncIOMotorClient # type: ignore # changed this line from "motor_asyncio" to "motor.motor_asyncio" to fix the error
from fastapi import FastAPI

DATABASE_URL = "mongodb://localhost:27017" # changed this line from "DATABASE_URL = "mongodb://mongo:27017"" to "DATABASE_URL = "mongodb://localhost:27017"" to fix the error

client = AsyncIOMotorClient(DATABASE_URL)
database = client.organization_db 

