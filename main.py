from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from services.supabase_client import supabase
app=FastAPI(title="Smart Emergency Backend")
class EmergencyCreate(BaseModel):
    user_id:str
    type:str
    description:str|None=None
    location:str


@app.get("/")
def home():
    return{"status":"Backend is running"}


@app.post("/emergency/create")
def create_emergency(data:EmergencyCreate):
    try:
        response=(
            supabase.table("emergencies")
            .insert({
                "user_id":data.user_id,
                "type":data.type,
                "description":data.description,
                "location":data.location,
            })
            .execute()
        )
        return{
            "message":"Emergency created successfully",
            "data":response.data
        }
    except Exception as e:
        raise HTTPException(status_code=500,
        detail=str(e))

