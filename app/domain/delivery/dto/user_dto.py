from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class CreateUserRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class UpdateUserRequest(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime
    updated_at: datetime

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
