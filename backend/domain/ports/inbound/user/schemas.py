from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from domain.schemas.enums import UserType, UserRole


class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    type: UserType
    bio: Optional[str] = None

class LoginRequest(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: str

class LoginResponse(BaseModel):
    access_token: str
    scheme: str = "bearer"

class EditUserInfoRequest(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    bio: Optional[str] = None

class RequestById(BaseModel):
    user_id: UUID