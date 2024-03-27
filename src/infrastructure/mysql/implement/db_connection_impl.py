from typing import Dict

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from src.infrastructure.mysql import IAsyncDbConnection


class DbConnectionFactory(object):
    _engines_by_url: Dict[str, AsyncEngine] = dict()

    @classmethod
    def get_engine(cls, username, password, host, port, db_name, isolation_level):
        url = f'mysql+aiomysql://{username}:{password}@{host}:{port}/{db_name}'
        if url not in cls._engines_by_url:
            engine = create_async_engine(url,
                                         echo=True,
                                         isolation_level=isolation_level,
                                         pool_size=1,
                                         max_overflow=0,
                                         pool_timeout=30,
                                         pool_pre_ping=True)
            cls._engines_by_url[url] = engine
        return cls._engines_by_url[url]


class MysqlDbConnection(IAsyncDbConnection):
    def __init__(self, db_name: str):
        username = "root"
        password = "root99"
        host = "localhost"
        port = "3306"
        self.engine = DbConnectionFactory.get_engine(username, password, host, port, db_name, self.isolation_level)

    def get_engine(self):
        return self.engine

    async def dispose(self) -> None:
        await self.engine.dispose()

    @property
    def isolation_level(self):
        return 'REPEATABLE READ'
