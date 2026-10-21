from uuid import UUID
from typing import Optional
from pydantic import BaseModel
from domain.schemas.core import Thread
from domain.ports.outbound.repo.abstract import Repo


class ThreadFilter(BaseModel):
    id: Optional[UUID] = None
    title: Optional[str] = None


class ThreadRepo(Repo[Thread, UUID, ThreadFilter]):
    pass