from typing import List
from abc import ABC, abstractmethod
from domain.schemas.core import Thread, Message, User
from domain.ports.inbound.thread.schemas import CreateThreadRequest, SendMessageRequest, GetThreadMessages, RequestById, \
    GetThreadsRequest


class ThreadManagementUseCase(ABC):

    @abstractmethod
    async def create_thread(self, request: CreateThreadRequest, actor: User) -> Thread:
        pass

    @abstractmethod
    async def close_thread(self, request: RequestById, actor: User) -> Thread:
        pass

    @abstractmethod
    async def get_all_threads(self, request: GetThreadsRequest) -> List[Thread]:
        pass

    @abstractmethod
    async def get_thread(self, request: RequestById) -> Thread:
        pass
    
    @abstractmethod
    async def get_threads_messages(self, request: GetThreadMessages) -> List[Message]:
        pass
    
    @abstractmethod
    async def send_message_to_thread(self, request: SendMessageRequest, actor: User) -> Message:
        pass