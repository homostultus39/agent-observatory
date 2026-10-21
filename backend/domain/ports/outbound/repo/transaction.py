from abc import ABC, abstractmethod
from typing import Self


class Transaction(ABC):
    @abstractmethod
    async def begin(self) -> None:
        pass

    @abstractmethod
    async def commit(self) -> None:
        pass

    @abstractmethod
    async def rollback(self) -> None:
        pass

    @abstractmethod
    async def close(self) -> None:
        pass

    async def __aenter__(self) -> Self:
        await self.begin()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is not None:
            await self.rollback()
        else:
            await self.commit()
        await self.close()


class TransactionFactory(ABC):
    @abstractmethod
    def create(self) -> Transaction:
        pass