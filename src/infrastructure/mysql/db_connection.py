from abc import ABC, abstractmethod
from typing import Type, TypeVar, Iterator, Optional

T = TypeVar('T', bound=object)


class IAsyncDbConnection(ABC):
    @abstractmethod
    def get_engine(self):
        raise NotImplementedError()

    @abstractmethod
    async def dispose(self) -> None:
        raise NotImplementedError()
