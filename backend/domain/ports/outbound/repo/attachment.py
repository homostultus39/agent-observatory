from uuid import UUID
from typing import Optional
from pydantic import BaseModel
from domain.schemas.core import Attachment
from domain.ports.outbound.repo.abstract import Repo


class AttachmentFilter(BaseModel):
    id: Optional[UUID] = None
    created_by_id: Optional[UUID] = None
    key: Optional[str] = None
    file_size: Optional[int] = None


class AttachmentRepo(Repo[Attachment, UUID, AttachmentFilter]):
    pass