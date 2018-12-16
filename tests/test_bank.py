from unittest import mock
from bank import Bank, ATMRegistry


def test_prototype():
    bank = Bank()
    atm_registry = ATMRegistry()
    for _ in range(3):
        bank.add_atm(atm_registry.get('rub'))
    for _ in range(4):
        bank.add_atm(atm_registry.get('usd'))
    assert len(bank.atms) == 7
    assert len([a for a in bank.atms if a.balance() == 1000]) == 3
    assert len([a for a in bank.atms if a.balance() == 100]) == 4


def test_observer():
    bank = Bank()
    atm_registry = ATMRegistry()
    atm = atm_registry.get('usd')
    bank.add_atm(atm)
    bank.update = mock.Mock()
    atm.withdraw(100)
    assert bank.update.called == True
