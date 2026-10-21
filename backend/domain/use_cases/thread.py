from datetime import datetime
from typing import List

from domain.exceptions import PermissionDeniedError, NotFoundError, ThreadAlreadyClosed
from domain.ports.inbound.thread.interface import ThreadManagementUseCase
from domain.ports.outbound.repo.thread import ThreadRepo
from domain.ports.outbound.repo.message import MessageRepo, MessageFilter
from domain.ports.outbound.repo.attachment import AttachmentRepo
from domain.ports.outbound.repo.transaction import TransactionFactory
from domain.schemas.core import Thread, Message, User
from domain.ports.inbound.thread.schemas import CreateThreadRequest, RequestById, GetThreadMessages, SendMessageRequest, \
    GetThreadsRequest
from domain.schemas.enums import UserRole


class ThreadUseCase(ThreadManagementUseCase):
    def __init__(
            self,
            thread_repo: ThreadRepo,
            message_repo: MessageRepo,
            attachment_repo: AttachmentRepo,
            transaction_factory: TransactionFactory,
    ):
        self._thread_repo = thread_repo
        self._message_repo = message_repo
        self._attachment_repo = attachment_repo
        self._transaction_factory = transaction_factory

    def _is_user_registered(self, actor: User) -> bool:
        return actor.role in UserRole

    def _is_admin(self, actor: User) -> bool:
        return actor.role == UserRole.ADMIN

    async def create_thread(self, request: CreateThreadRequest, actor: User) -> Thread:
        new_thread = Thread(
            title=request.title,
            created_by_id=actor.id,
            created_at=datetime.now(),
            updated_at=datetime.now(),

        )
        await self._thread_repo.create(new_thread)
        return new_thread

    async def close_thread(self, request: RequestById, actor: User) -> Thread:
        if not self._is_admin(actor):
            raise PermissionDeniedError("Only Admin can close thread")
        async with self._transaction_factory.create() as transaction:
            thread = await self._thread_repo.get(request.thread_id, transaction=transaction)
            if thread is None:
                raise NotFoundError(f"Thread {request.thread_id} not found")
            if thread.closed_at is not None:
                raise ThreadAlreadyClosed(f"Thread f{request.thread_id} already closed")

            now = datetime.now()
            updated = await self._thread_repo.update(
                obj_pk=request.thread_id,
                values={
                    "closed_by_id": actor.id,
                    "closed_at": now,
                    "updated_at": now,
                },
                transaction=transaction,
            )
            if updated is None:
                raise NotFoundError(f"Thread {request.thread_id} not found")
        return thread

    async def get_all_threads(self, request: GetThreadsRequest) -> List[Thread]:
        return await self._thread_repo.get_all(offset=request.offset, limit=request.limit)

    async def get_thread(self, request: RequestById) -> Thread:
        thread = await self._thread_repo.get(request.thread_id)
        if thread is None:
            raise NotFoundError(f"Thread {request.thread_id} not found")
        return thread

    async def get_threads_messages(self, request: GetThreadMessages) -> List[Message]:
        messages = await self._message_repo.filter(
            MessageFilter(thread_id=request.thread_id),
            limit=request.limit,
            offset=request.offset,
        )
        return messages
    
    async def send_message_to_thread(self, request: SendMessageRequest, actor: User) -> Message:
        if not self._is_user_registered(actor):
            raise PermissionDeniedError("Only registered users can send message to thread")
        async with self._transaction_factory.create() as transaction:
            message = Message(
                author_id=actor.id,
                thread_id=request.thread_id,
                body=request.body,
                attachments_id=request.attachment_ids,
                created_at=datetime.now(),
            )
            await self._message_repo.create(
                message,
                transaction=transaction,
            )

            thread = await self._thread_repo.get(obj_pk=request.thread_id, transaction=transaction)
            await self._thread_repo.update(
                obj_pk=request.thread_id,
                values={
                    "count_message": thread.count_message + 1
                }
            )
            await transaction.commit()

        return message