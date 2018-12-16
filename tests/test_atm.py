from itertools import permutations

import pytest

from atm import DollarATM
from cassette import DollarCassette, NotEnoughBanknotes


@pytest.mark.parametrize("withdraws", [
    [198],
    [121, 5, 50],
    [111, 5, 60],
    [131, 5, 50],
    [131, 5, 61],
    [131, 5, 62],
    [131, 5, 62],
])
def test_withdraw(withdraws):
    for ws in permutations(withdraws):
        atm = DollarATM([
            DollarCassette(1, 3),
            DollarCassette(5, 1),
            DollarCassette(10, 2),
            DollarCassette(20, 1),
            DollarCassette(50, 1),
            DollarCassette(100, 1),
        ])
        for w in ws:
            atm.withdraw(w)


@pytest.mark.parametrize("withdraws", [
    [600],
    [200],
    [199],
    [198, 1],
    [190, 4],
    [4],
    [131, 5, 63],
    [132, 5, 62],
])
def test_withdraw_fails(withdraws):
    for ws in permutations(withdraws):
        atm = DollarATM([
            DollarCassette(1, 3),
            DollarCassette(5, 1),
            DollarCassette(10, 2),
            DollarCassette(20, 1),
            DollarCassette(50, 1),
            DollarCassette(100, 1),
        ])
        with pytest.raises(NotEnoughBanknotes):
            for w in ws:
                atm.withdraw(w)
