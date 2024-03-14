from typing import Dict

import sqlalchemy


class DbContext(object):
    _engines_by_url: Dict[str, sqlalchemy.engine.Engine] = dict()

    def __init__(self):
        username = "root"
        password = "1234"
        host = "localhost"
        port = "3306"
        self.connection = self._get_engine(username, password, host, port)

    def _get_engine(self, username, password, host, port):
        url = f'mysql+pymysql://{username}:{password}@{host}:{port}'
        if url not in self.__class__._engines_by_url:
            isolation_level = self._get_isolation_level()
            engine = sqlalchemy.engine.create_engine(url,
                                                     echo=True,
                                                     isolation_level=isolation_level,
                                                     pool_size=1,
                                                     max_overflow=0,
                                                     pool_timeout=30,
                                                     pool_pre_ping=True)
            self._engines_by_url[url] = engine
        return self._engines_by_url[url]

    def _get_isolation_level(self):
        return 'REPEATABLE READ'
