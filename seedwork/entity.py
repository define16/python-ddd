import hashlib
import uuid


class Entity:
    id: str  # Entity 식별자
    seq: int  # DB 시퀀스 -> DB primary key와 auto increment와 연동

    def __init__(self):
        self.id: str = str(uuid.uuid4())

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
