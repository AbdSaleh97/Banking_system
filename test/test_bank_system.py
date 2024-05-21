##tests for Account and saving account
import pytest
from bank_system.account import Account
from bank_system.Saving_account import SavingsAccount

@pytest.fixture
def account_instance():
    return Account("12345", 100.0)

@pytest.fixture
def savings_account_instance():
    return SavingsAccount("67890", 200.0, 0.05)

def test_account_creation(account_instance):
    assert account_instance._Account__account_number == "12345"
    assert account_instance._Account__balance == 100.0

def test_deposit_and_withdraw(account_instance):
    account_instance.deposite(50.0)
    assert account_instance._Account__balance == 150.0
    account_instance.withdraw(30.0)
    assert account_instance._Account__balance == 120.0

def test_transfer(account_instance):
    to_account = Account("54321", 50.0)
    account_instance.transfer(to_account, 30.0)
    assert account_instance._Account__balance == 70.0
    assert to_account._Account__balance == 80.0

def test_insufficient_funds(account_instance, capsys):
    account_instance.withdraw(200.0)
    captured = capsys.readouterr()
    assert "Insufficient funds" in captured.out

def test_account_str(account_instance):
    assert str(account_instance) == "Checking Account Number: 12345, Balance: 100.0"

def test_savings_account_creation(savings_account_instance):
    assert savings_account_instance._Account__account_number == "67890"
    assert savings_account_instance._Account__balance == 200.0
    assert savings_account_instance.interest_rate == 0.05

def test_calculate_and_deposit_interest(savings_account_instance):
    assert savings_account_instance.calculate_interest() == 10.0
    savings_account_instance.deposit_interest()
    assert savings_account_instance._Account__balance == 210.0

def test_savings_account_str(savings_account_instance):
    assert str(savings_account_instance) == "Savings Account Number: 67890, Balance: 200.0"
 