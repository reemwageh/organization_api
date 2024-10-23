from fastapi import FastAPI
from auth import router as auth_router # changed this line from "from auth import router" to "from auth import router as auth_router" to fix the error
from organizations import router as org_router # changed this line from "from organizations import router" to "from organizations import router as org_router" to fix the error

app = FastAPI()

app.include_router(auth_router) # changed this line from "app.include_router(auth)" to "app.include_router(auth_router)" to fix the error
app.include_router(org_router) # changed this line from "app.include_router(organizations)" to "app.include_router(org_router)" to fix the error

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Organization API"}
