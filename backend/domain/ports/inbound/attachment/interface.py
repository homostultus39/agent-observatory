from abc import ABC, abstractmethod
from domain.schemas.core import Attachment
from domain.ports.inbound.attachment.schemas import AddAttachmentRequest, RequestById


class AttachmentUseCase(ABC):
    @abstractmethod
    async def add_attachment(self, request: AddAttachmentRequest) -> Attachment:
        pass

    @abstractmethod
    async def delete_attachment(self, request: RequestById) -> bool:
        pass