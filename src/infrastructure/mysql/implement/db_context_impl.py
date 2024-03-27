from sqlalchemy.ext.asyncio import async_sessionmaker, async_scoped_session

from src.infrastructure.mysql import IDbContext
from src.infrastructure.mysql.db_connection import IAsyncDbConnection


class DbContext(IDbContext):

    def __init__(self, connection: IAsyncDbConnection):
        self.connection = connection.get_engine()
        self._async_session_factory = async_sessionmaker(bind=self.connection, expire_on_commit=False)
        self._session = self._async_session_factory()
        # self._session = async_scoped_session(
        #     session_factory=self._async_session_factory,
        #     scopefunc=current_task,
        # )
        # self._session = self._async_session_factory

    @property
    def session(self):
        return self._session

    async def commit_and_expunge_all(self):
        await self.session.commit()
        self.session.expunge_all()

    async def close_session(self):
        await self._session.close()

    # def close_session(self):
    #     # async_scoped_session 시작
    #     self._session.remove()
