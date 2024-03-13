import uuid


class Entity:
    __id: str  # Entity 식별자
    __seq: int  # DB 시퀀스 -> DB primary key와 auto increment와 연동

    def __init__(self):
        self.__id: str = str(uuid.uuid4())

    def __eq__(self, other):
        if isinstance(self, other):
            return self.__id == other.id
        return False

    def __hash__(self):
        return hash(self.__id)

    @property
    def id(self) -> str:
        return self.__id

    @property
    def seq(self) -> int:
        return self.__seq
