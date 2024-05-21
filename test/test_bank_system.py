
from bank_system.account import Account
from bank_system.Saving_account import SavingsAccount
from bank_system.loan import Loan
import pytest

@pytest.fixture
def account_instance():
    """Fixture to create a checking account instance."""
    class CheckingAccount(Account):
        def deposit(self, amount):
            """Deposit money into the checking account."""
            if amount > 0:
                new_balance = self.get_balance() + amount
                self._set_balance(new_balance)

        def withdraw(self, amount):
            """Withdraw money from the checking account."""
            if 0 < amount <= self.get_balance():
                new_balance = self.get_balance() - amount
                self._set_balance(new_balance)
            else:
                raise ValueError("Insufficient funds")
    
    return CheckingAccount("12345", 100.0)

@pytest.fixture
def savings_account_instance():
    """Fixture to create a savings account instance."""
    return SavingsAccount("67890", 200.0, 0.05)

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
    class CheckingAccount(Account):
        def deposit(self, amount):
            """Deposit money into the checking account."""
            if amount > 0:
                new_balance = self.get_balance() + amount
                self._set_balance(new_balance)

        def withdraw(self, amount):
            """Withdraw money from the checking account."""
            if 0 < amount <= self.get_balance():
                new_balance = self.get_balance() - amount
                self._set_balance(new_balance)
            else:
                raise ValueError("Insufficient funds")
    
    to_account = CheckingAccount("54321", 50.0)
    account_instance.transfer(to_account, 30.0)
    assert account_instance.get_balance() == 70.0
    assert to_account.get_balance() == 80.0

def test_insufficient_funds(account_instance):
    """Test handling of insufficient funds during withdrawal."""
    with pytest.raises(ValueError, match="Insufficient funds"):
        account_instance.withdraw(200.0)

def test_account_str(account_instance):
    """Test the string representation of an account."""
    assert str(account_instance) == "Checking Account Number: 12345, Balance: 100.0"

def test_savings_account_creation(savings_account_instance):
    """Test the creation of a savings account."""
    assert savings_account_instance.get_account_number() == "67890"
    assert savings_account_instance.get_balance() == 200.0
    assert savings_account_instance.get_interest_rate() == 0.05

def test_calculate_and_deposit_interest(savings_account_instance):
    """Test the calculation and deposit of interest."""
    assert savings_account_instance.calculate_interest() == 10.0
    savings_account_instance.deposit_interest()
    assert savings_account_instance.get_balance() == 210.0

def test_savings_account_str(savings_account_instance):
    """Test the string representation of a savings account."""
    assert str(savings_account_instance) == "Savings Account Number: 67890, Balance: 200.0, Interest Rate: 0.05"

###
import pytest
from bank_system.loan import Loan  # Import the Loan class from your module

@pytest.fixture
def loan_instance():
    # Create a Loan instance with some initial values for testing
    customer = "John Doe"
    amount = 1000
    interest_rate = 0.1
    return Loan(customer, amount, interest_rate)

def test_make_payment(loan_instance):
    
    loan_instance.make_payment(500)  
    assert loan_instance._Loan__remaining_balance == 500  

   
    loan_instance.make_payment(300)  
    assert loan_instance._Loan__remaining_balance == 200  

   
    loan_instance.make_payment(300) 
    assert loan_instance._Loan__remaining_balance >= 0 