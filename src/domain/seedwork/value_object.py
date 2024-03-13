from dataclasses import dataclass


@dataclass(frozen=True)
class ValueObject:
    def __eq__(self, other):
        raise NotImplementedError

    def __hash__(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError
