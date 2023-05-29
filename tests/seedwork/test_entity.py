from dataclasses import dataclass

from seedwork.entity import Entity
from seedwork.value_object import ValueObject


class MockEntity(Entity):
    name: str

    def __init__(self, name):
        super().__init__()
        self.name = name

    def update(self, name):
        self.name = name


def test_same_entity():
    v1 = MockEntity(
        name="name",
    )

    v2 = MockEntity(
        name="name",
    )

    assert v1 != v2, "id가 서로 다르기 때문에 엔티티가 같으면 안된다."


def test_update_entity():
    v1 = MockEntity(
        name="name",
    )

    new = v1
    new.update(name="new")

    assert v1 == new, "id가 서로 같기 때문에 엔티티가 같아야한다."
