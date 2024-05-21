import pytest
from bank_system.account import Account
from bank_system.Saving_account import SavingsAccount

class TestAccount(Account):
    def deposit(self, amount):
        self._set_balance(self.get_balance() + amount)

    def withdraw(self, amount):
        if self.get_balance() >= amount:
            self._set_balance(self.get_balance() - amount)
        else:
            raise ValueError("Insufficient funds")

@pytest.fixture
def account_instance():
    return TestAccount("12345", 100.0)

@pytest.fixture
def savings_account_instance():
    return SavingsAccount("67890", 200.0, 0.05)

def test_deposit_and_withdraw(account_instance):
    account_instance.deposit(50.0)
    assert account_instance.get_balance() == 150.0
    account_instance.withdraw(30.0)
    assert account_instance.get_balance() == 120.0

def test_transfer(account_instance):
    to_account = TestAccount("54321", 50.0)
    account_instance.transfer(to_account, 30.0)
    assert account_instance.get_balance() == 70.0
    assert to_account.get_balance() == 80.0

def test_insufficient_funds(account_instance):
    with pytest.raises(ValueError, match="Insufficient funds"):
        account_instance.withdraw(200.0)

def test_account_str(account_instance):
    assert str(account_instance) == "Checking Account Number: 12345, Balance: 100.0"
