from uuid import UUID
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr
from domain.schemas.enums import UserType, UserRole


class User(BaseModel):
    id: Optional[UUID] = None
    username: str
    email: EmailStr
    password_hash: str
    type: UserType

    role: UserRole
    bio: Optional[str] = None

class Attachment(BaseModel):
    id: Optional[UUID] = None
    created_by_id: UUID

    bucket_name: str
    key: str

    original_name: str
    content_type: str
    file_size: int
    
    created_at: datetime
    
class Thread(BaseModel):
    id: Optional[UUID] = None

    title: str
    created_by_id: UUID

    count_message: int = 0

    created_at: datetime
    updated_at: datetime

    closed_by_id: Optional[UUID] = None
    closed_at: Optional[datetime] = None

class Message(BaseModel):
    id: Optional[UUID] = None
    author_id: UUID
    thread_id: UUID
    body: str
    attachments_id: List[UUID] = []
    created_at: datetime
    edited_at: Optional[datetime] = None