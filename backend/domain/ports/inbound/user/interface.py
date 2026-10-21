from abc import ABC, abstractmethod
from domain.schemas.core import User
from domain.ports.inbound.user.schemas import RegisterRequest, LoginRequest, LoginResponse, EditUserInfoRequest, RequestById


class UserManagementUseCase(ABC):
    @abstractmethod
    async def register(self, request: RegisterRequest) -> User:
        pass

    @abstractmethod
    async def login(self, reqest: LoginRequest) -> LoginResponse:
        pass

    @abstractmethod
    async def refresh(self) -> LoginResponse:
        pass

    @abstractmethod
    async def edit_user_info(self, reqest: EditUserInfoRequest) -> int:
        pass

    @abstractmethod
    async def block_user(self, request: RequestById) -> bool:
        pass