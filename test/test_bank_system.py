from bank_system.account import Account
from bank_system.loan import Loan
from bank_system.customer import Customer
import pytest

@pytest.fixture
def account_instance():
    """Fixture to create a checking account instance."""
    class TestAccount(Account):
        def deposit(self, amount):
            self._balance += amount

        def withdraw(self, amount):
            if self._balance >= amount:
                self._balance -= amount
            else:
                raise ValueError("Insufficient funds")

    return TestAccount("12345", 100.0)

@pytest.fixture
def savings_account_instance():
    """Fixture to create a savings account instance."""
    class SavingsAccount(Account):
        def deposit(self, amount):
            self._balance += amount

        def withdraw(self, amount):
            if self._balance >= amount:
                self._balance -= amount
            else:
                raise ValueError("Insufficient funds")

    return SavingsAccount("67890", 200.0)


def test_account_creation(account_instance):
    """Test the creation of an account."""
    assert account_instance.get_account_number() == "12345"
    assert account_instance.get_balance() == 100.0


def test_deposit_and_withdraw(account_instance):
    """Test deposit and withdrawal operations."""
    account_instance.deposit(50.0)
    assert account_instance.get_balance() == 150.0
    account_instance.withdraw(30.0)
    assert account_instance.get_balance() == 120.0


def test_transfer(account_instance):
    """Test transferring money between accounts."""
    to_account = Account("54321", 50.0)
    account_instance.transfer(to_account, 30.0)
    assert account_instance.get_balance() == 70.0
    assert to_account.get_balance() == 80.0


def test_insufficient_funds(account_instance):
    """Test handling of insufficient funds during withdrawal."""
    with pytest.raises(ValueError, match="Insufficient funds"):
        account_instance.withdraw(200.0)


def test_account_str(account_instance):
    """Test the string representation of an account."""
    assert str(account_instance) == "Account Number: 12345, Balance: 100.0"


def test_savings_account_creation(savings_account_instance):
    """Test the creation of a savings account."""
    assert savings_account_instance.get_account_number() == "67890"
    assert savings_account_instance.get_balance() == 200.0


def test_loan_instance():
    """Test the creation of a loan."""
    customer = Customer("John Doe", "123 Elm St", "555-1234")
    loan_instance = Loan(customer, 1000, 0.1)
    assert loan_instance.customer == customer
    assert loan_instance.amount == 1000
    assert loan_instance.interest_rate == 0.1


def test_make_payment():
    """Test making payments on a loan."""
    customer = Customer("John Doe", "123 Elm St", "555-1234")
    loan_instance = Loan(customer, 1000, 0.1)
    
    loan_instance.make_payment(500)
    assert loan_instance.remaining_balance == 500

    loan_instance.make_payment(300)
    assert loan_instance.remaining_balance == 200

    loan_instance.make_payment(300)
    assert loan_instance.remaining_balance >= 0
