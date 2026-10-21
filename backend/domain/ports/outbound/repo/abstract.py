from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List, Dict, Any
from domain.ports.outbound.repo.transaction import Transaction

TDomain = TypeVar("TDomain")
TPk = TypeVar("TPk")
TFilter = TypeVar("TFilter")


class Repo(ABC, Generic[TDomain, TPk, TFilter]):
    @abstractmethod
    async def count(
        self,
        filters: TFilter,
        transaction: Optional[Transaction] = None
    ) -> int:
        pass

    @abstractmethod
    async def create(
        self,
        obj: TDomain,
        transaction: Optional[Transaction] = None
    ) -> TDomain:
        pass
    
    @abstractmethod
    async def get(
        self,
        obj_pk: TPk,
        transaction: Optional[Transaction] = None
    ) -> Optional[TDomain]:
        pass

    @abstractmethod
    async def get_all(
        self,
        limit: int = 50,
        offset: int = 0,
        transaction: Optional[Transaction] = None
    ) -> List[TDomain]:
        pass

    @abstractmethod
    async def filter(
        self,
        filters: TFilter,
        limit: int = 50,
        offset: int = 0,
        transaction: Optional[Transaction] = None
    ) -> List[TDomain]:
        pass

    @abstractmethod
    async def update(
        self,
        obj_pk: TPk,
        values: Dict[str, Any],
        transaction: Optional[Transaction] = None
    ) -> Optional[TDomain]:
        pass

    @abstractmethod
    async def delete(
        self,
        id: TPk,
        transaction: Optional[Transaction] = None
    ) -> bool:
        pass