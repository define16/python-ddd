from abc import ABC


class Repository(ABC):
    def add(self):
        raise NotImplementedError()

    def next_identity(self):
        raise NotImplementedError
