from abc import ABC, abstractmethod
from enum import Enum

from typing import Optional


class Currency(Enum):
    RUBLE = 1
    DOLLAR = 2


class NotEnoughBanknotes(Exception):
    pass


class Cassette(ABC):
    @abstractmethod
    def __init__(self, nominal_value: int, banknotes: int, currency: Currency):
        self.currency: Currency = currency
        self.nominal_value: int = nominal_value
        self.banknotes: int = banknotes
        self._next_cassette: Optional[Cassette] = None

    def set_next_cassette(self, next_cassete):
        self._next_cassette = next_cassete

    def withdraw(self, amount: int) -> None:
        banknotes = min(amount // self.nominal_value, self.banknotes)
        amount = amount - banknotes * self.nominal_value
        if self._next_cassette is not None:
            self._next_cassette.withdraw(amount)
        else:
            if amount != 0:
                raise NotEnoughBanknotes()
        self.banknotes -= banknotes


class RubleCassette(Cassette):
    def __init__(self, nominal_value: int, banknotes: int):
        super().__init__(nominal_value, banknotes, Currency.RUBLE)


class DollarCassette(Cassette):
    def __init__(self, nominal_value: int, banknotes: int):
        super().__init__(nominal_value, banknotes, Currency.DOLLAR)
