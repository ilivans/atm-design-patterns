from abc import ABC, abstractmethod
from copy import deepcopy

from typing import List

from cassette import Cassette, DollarCassette, RubleCassette
from iterator import ListCollection
from interfaces import Prototype, Observer


class ATM(ABC):
    @abstractmethod
    def __init__(self, cassettes: List[Cassette]):
        # Cassettes currencies must be the same
        assert len(set(c.currency for c in cassettes)) <= 1
        # Sort by nominal value and build chain of responsibility
        cassettes = list(sorted(cassettes, key=lambda c: c.nominal_value, reverse=True))
        for i in range(len(cassettes) - 1):
            cassettes[i].set_next_cassette(cassettes[i + 1])
        if len(cassettes):
            cassettes[-1].set_next_cassette(None)
        self._cassettes: ListCollection = ListCollection(cassettes)
        self._observers = []

    def withdraw(self, amount: int) -> None:
        """
        Withdraw money using ATM
        
        Assumes that client has enough money on his account (it was checked before the operation)
        :param amount: total amount of money to withdraw 
        :return: 0 if successful
        :raise NotEnoughBanknotes: not enough banknotes in the ATM to perform the operation
        """
        self._cassettes.create_iterator().next().withdraw(amount)  # Chain of responsibility
        # Notify bank about empty cassette
        iterator = self._cassettes.create_iterator()
        while iterator.has_next():
            if iterator.next().banknotes == 0:
                for observer in self._observers:
                    observer.update(self)
                break

    def balance(self) -> int:
        iterator = self._cassettes.create_iterator()
        balance = 0
        while iterator.has_next():
            cassette = iterator.next()
            balance += cassette.nominal_value * cassette.banknotes
        return balance

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def get_state(self):
        return self._cassettes


class DollarATM(ATM, Prototype):
    def __init__(self, cassettes: List[DollarCassette]):
        super().__init__(cassettes)

    def clone(self):
        return deepcopy(self)


class RubleATM(ATM, Prototype):
    def __init__(self, cassettes: List[RubleCassette]):
        super().__init__(cassettes)

    def clone(self):
        return deepcopy(self)
