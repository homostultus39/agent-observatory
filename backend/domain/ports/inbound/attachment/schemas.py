from pydantic import BaseModel
from uuid import UUID


class AddAttachmentRequest(BaseModel):
    content: bytes
    original_name: str

class RequestById(BaseModel):
    attachment_id: UUID