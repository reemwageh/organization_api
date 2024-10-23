from fastapi import FastAPI
from auth import router as auth_router 
from organizations import router as org_router 
app = FastAPI()

app.include_router(auth_router) 
app.include_router(org_router) 

@app.get("/")
async def read_root():
    """
    Root endpoint providing a welcome message.
    """
    return {"message": "Welcome to the Organization API"}