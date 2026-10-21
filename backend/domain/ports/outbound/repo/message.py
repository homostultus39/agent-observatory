from uuid import UUID
from typing import Optional
from pydantic import BaseModel
from domain.schemas.core import Message
from domain.ports.outbound.repo.abstract import Repo


class MessageFilter(BaseModel):
    id: Optional[UUID] = None
    author_id: Optional[UUID] = None
    thread_id: Optional[UUID] = None


class MessageRepo(Repo[Message, UUID, MessageFilter]):
    pass