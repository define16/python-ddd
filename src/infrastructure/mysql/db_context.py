from typing import Dict
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker, async_scoped_session


class DbContext(object):
    _engines_by_url: Dict[str, AsyncEngine] = dict()

    def __init__(self):
        username = "root"
        password = "root99"
        host = "localhost"
        port = "3306"
        self.connection = self._get_engine(username, password, host, port)
        self._async_session_factory = async_sessionmaker(bind=self.connection, expire_on_commit=False)
        self._session = self._async_session_factory()
        # self._session = async_scoped_session(
        #     session_factory=self._async_session_factory,
        #     scopefunc=current_task,
        # )
        # self._session = self._async_session_factory

    def _get_engine(self, username, password, host, port):
        url = f'mysql+aiomysql://{username}:{password}@{host}:{port}/python-ddd'
        if url not in self.__class__._engines_by_url:
            engine = create_async_engine(url,
                                         echo=True,
                                         isolation_level=self.isolation_level,
                                         pool_size=1,
                                         max_overflow=0,
                                         pool_timeout=30,
                                         pool_pre_ping=True)
            self._engines_by_url[url] = engine
        return self._engines_by_url[url]

    @property
    def isolation_level(self):
        return 'REPEATABLE READ'

    @property
    def session(self):
        return self._session

    # def close_session(self):
    #     # async_scoped_session 시작
    #     self._session.remove()

    async def commit_and_expunge_all(self):
        await self.session.commit()
        self.session.expunge_all()

    async def close_session(self):
        await self._session.close()
