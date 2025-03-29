from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models import authenticate

auth_router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@auth_router.post("/login")
def login(request: LoginRequest):
    if authenticate(request.username, request.password):
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
