from abc import ABC, abstractmethod


class IDbContext(ABC):

    @abstractmethod
    @property
    def session(self):
        raise NotImplementedError

    @abstractmethod
    async def commit_and_expunge_all(self):
        raise NotImplementedError

    @abstractmethod
    async def close_session(self):
        raise NotImplementedError
