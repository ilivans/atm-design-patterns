from typing import Dict

from atm import RubleATM, DollarATM, ATM, Prototype
from cassette import RubleCassette, DollarCassette
from interfaces import Observer


class ATMRegistry:
    def __init__(self):
        # The initialization could be moved out
        self._atms: Dict[str, Prototype] = {
            'rub': RubleATM([RubleCassette(1000, 1)]),
            'usd': DollarATM([DollarCassette(100, 1)])
        }

    def get(self, key: str) -> ATM:
        return self._atms[key].clone()


class Bank(Observer):
    def __init__(self):
        super().__init__()
        self.atms = []

    def add_atm(self, atm: ATM):
        self.atms.append(atm)
        atm.attach(self)

    def update(self, atm: ATM):
        cassettes = atm.get_state()
        # Do something about empty cassette
