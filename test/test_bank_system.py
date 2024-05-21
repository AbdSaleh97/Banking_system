from bank_system.bank import BankingSystem
from bank_system.customer import Customer
from bank_system.account import Account

import pytest

@pytest.fixture
def banking_system():
    return BankingSystem()

@pytest.fixture
def customer():
    return Customer("John Doe", "123 Elm St", "555-1234")

@pytest.fixture
def account():
    # Assuming there is a concrete subclass of Account for testing purposes
    class TestAccount(Account):
        def deposit(self, amount):
            self._set_balance(self.get_balance() + amount)

        def withdraw(self, amount):
            if self.get_balance() >= amount:
                self._set_balance(self.get_balance() - amount)
            else:
                raise ValueError("Insufficient funds")

    return TestAccount("ACC123", 1000)

def test_add_customer(banking_system):
    customer = banking_system.add_customer("John Doe")
    assert customer is not None
    assert customer.get_name() == "John Doe"
    assert banking_system.get_customers()[banking_system.get_customer_id()] == customer

def test_add_existing_customer(banking_system):
    banking_system.add_customer("John Doe")
    customer = banking_system.add_customer("John Doe")
    assert customer is None

def test_add_account(banking_system, account):
    banking_system.add_customer("John Doe")
    account = banking_system.add_account("ACC123", 1000)
    assert account is not None
    assert account.get_account_number() == "ACC123"
    assert account.get_balance() == 1000
    assert account in banking_system.get_accounts()[banking_system.get_customer_id()]

def test_add_account_without_customer(banking_system, account):
    account = banking_system.add_account("ACC123", 1000)
    assert account is None

def test_delete_account(banking_system, account):
    banking_system.add_customer("John Doe")
    account = banking_system.add_account("ACC123", 1000)
    banking_system.delete_account(banking_system.get_customer_id(), "ACC123")
    assert account not in banking_system.get_accounts()[banking_system.get_customer_id()]

def test_delete_non_existent_account(banking_system):
    banking_system.add_customer("John Doe")
    banking_system.delete_account(banking_system.get_customer_id(), "NON_EXISTENT")
    assert True  # Just checking that no exception is raised

def test_get_customer_accounts(banking_system, account):
    banking_system.add_customer("John Doe")
    banking_system.add_account("ACC123", 1000)
    accounts = banking_system.get_customer_accounts(banking_system.get_customer_id())
    assert len(accounts) == 1
    assert accounts[0].get_account_number() == "ACC123"

def test_get_customer_accounts_no_customer(banking_system):
    accounts = banking_system.get_customer_accounts("NON_EXISTENT")
    assert accounts is None

def test_delete_user(banking_system, account):
    banking_system.add_customer("John Doe")
    banking_system.add_account("ACC123", 1000)
    result = banking_system.delete_user(banking_system.get_customer_id())
    assert result == "Customer deleted successfully with all associated accounts."
    assert banking_system.get_customer_id() not in banking_system.get_customers()

def test_delete_non_existent_user(banking_system):
    result = banking_system.delete_user("NON_EXISTENT")
    assert result == "Customer does not exist."

def test_customer_info(customer):
    info = customer.get_customer_info()
    assert info['name'] == "John Doe"
    assert info['address'] == "123 Elm St"
    assert info['phone_number'] == "555-1234"
