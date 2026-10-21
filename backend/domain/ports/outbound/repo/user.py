from uuid import UUID
from typing import Optional
from pydantic import BaseModel, EmailStr
from domain.schemas.core import User
from domain.schemas.enums import UserRole, UserType
from domain.ports.outbound.repo.abstract import Repo


class UserFilter(BaseModel):
    id: Optional[UUID] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    type: Optional[UserType] = None
    role: Optional[UserRole] = None


class UserRepo(Repo[User, UUID, UserFilter]):
    pass