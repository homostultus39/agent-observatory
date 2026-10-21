from typing import Optional, List

from pydantic import BaseModel, Field
from uuid import UUID


class CreateThreadRequest(BaseModel):
    title: str

class SendMessageRequest(BaseModel):
    thread_id: UUID
    body: str
    attachment_ids: List[UUID] = []

class GetThreadsRequest(BaseModel):
    offset: int = Field(0, ge=0)
    limit: int = Field(50, ge=1, le=100)

class GetThreadMessages(BaseModel):
    thread_id: UUID
    offset: int = Field(0, ge=0)
    limit: int = Field(50, ge=1, le=100)

class RequestById(BaseModel):
    thread_id: UUID