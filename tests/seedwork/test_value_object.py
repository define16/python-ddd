from dataclasses import dataclass

from src.domain.seedwork import ValueObject


@dataclass(frozen=True)
class MockValueObject(ValueObject):
    name: str
    seq: int
    data_dict: dict
    data_list: list


def test_same_value_object():
    v1 = MockValueObject(
        name="name",
        seq=1,
        data_dict={1: 2, 2: 3},
        data_list=[1, 2, 3]
    )

    v2 = MockValueObject(
        name="name",
        seq=1,
        data_dict={1: 2, 2: 3},
        data_list=[1, 2, 3]
    )

    v3 = MockValueObject(
        name="name",
        seq=1,
        data_dict={2: 3, 1: 2},
        data_list=[1, 2, 3]
    )

    v4 = MockValueObject(
        name="name",
        seq=1,
        data_dict={1: 2, 2: 3},
        data_list=[1, 3, 2]
    )

    v5 = MockValueObject(
        name="name",
        seq=2,
        data_dict={1: 2, 2: 3},
        data_list=[1, 2, 3]
    )

    assert v1 == v2, "완전히 같은 값을 갖는 값 객체가 아닙니다."
    assert v1 == v3, "Dict는 순서가 중요하지 않기 때문에 값 객체가 같아야합니다."
    assert v1 != v4, "List는 순서가 중요하기 때문에 값 객체는 서로 달라야합니다."
    assert v1 != v5, "내부값이 다르기 때문에 값 객체는 서로 달라야합니다."
