from abc import abstractmethod, ABC


class Prototype(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def clone(self):
        pass


class Observer(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def update(self, subject):
        pass
