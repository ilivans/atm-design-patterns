from abc import ABC, abstractmethod
from typing import Sequence, TypeVar, List

T = TypeVar('T')


class Iterator(ABC):
    @abstractmethod
    def __init__(self, collection: Sequence[T]):
        self._collection: Sequence = collection
        self._total_size = len(collection)
        self._elements_exposed = 0

    @abstractmethod
    def next(self) -> T:
        pass

    def has_next(self):
        return self._elements_exposed < self._total_size


class ListIterator(Iterator):
    def __init__(self, collection: List[T]):
        super().__init__(collection)

    def next(self) -> T:
        if self.has_next():
            self._elements_exposed += 1
            return self._collection[self._elements_exposed - 1]
        else:
            raise StopIteration


class Collection(ABC):
    @abstractmethod
    def __init__(self, collection: Sequence[T]):
        self._collection: Sequence[T] = collection

    @abstractmethod
    def create_iterator(self):
        pass


class ListCollection(Collection):
    def __init__(self, collection: List[T]):
        super().__init__(collection)

    def create_iterator(self):
        return ListIterator(self._collection)
