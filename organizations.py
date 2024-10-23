from typing import List
from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException
from schemas import OrganizationCreate, OrganizationRead, UserInvite 
from database import database 
from utils import get_current_user  

router = APIRouter()

@router.post("/organization", response_model=OrganizationRead, dependencies=[Depends(get_current_user)])
async def create_organization(org: OrganizationCreate):
    new_org = {
        "name": org.name,
        "description": org.description,
        "organization_members": []
    }
    result = await database["organizations"].insert_one(new_org)
    
    return OrganizationRead(organization_id=str(result.inserted_id), name=org.name, description=org.description)

@router.get("/organization/{organization_id}", response_model=OrganizationRead, dependencies=[Depends(get_current_user)])
async def read_organization(organization_id: str):
    org = await database["organizations"].find_one({"_id": ObjectId(organization_id)})
    if org is None:
        raise HTTPException(status_code=404, detail="Organization not found")

    return OrganizationRead(
        organization_id=organization_id,
        name=org["name"],
        description=org["description"],
        organization_members=org["organization_members"]
    )

@router.get("/organization", response_model=List[OrganizationRead], dependencies=[Depends(get_current_user)])
async def read_all_organizations():
    orgs = await database["organizations"].find().to_list(100)
    return [OrganizationRead(
        organization_id=str(org["_id"]),
        name=org["name"],
        description=org["description"],
        organization_members=org["organization_members"]
    ) for org in orgs]

@router.put("/organization/{organization_id}", response_model=OrganizationRead, dependencies=[Depends(get_current_user)])
async def update_organization(organization_id: str, org: OrganizationCreate):
    result = await database["organizations"].update_one(
        {"_id": ObjectId(organization_id)},
        {"$set": {"name": org.name, "description": org.description}}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Organization not found")

    return OrganizationRead(organization_id=organization_id, name=org.name, description=org.description)

@router.delete("/organization/{organization_id}", dependencies=[Depends(get_current_user)])
async def delete_organization(organization_id: str):
    result = await database["organizations"].delete_one({"_id": ObjectId(organization_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Organization not found")

    return {"message": "Organization deleted successfully"}

@router.post("/organization/{organization_id}/invite", dependencies=[Depends(get_current_user)])
async def invite_user_to_organization(organization_id: str, user: UserInvite):
    return {"message": "User invited successfully"}
