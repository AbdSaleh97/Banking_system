import pytest
from datetime import datetime, timedelta
from bank_system.check_account import CheckingAccount  # Replace 'your_module' with the actual name of your module

# Test case for initializing a CheckingAccount
def test_checking_account_initialization():
    account = CheckingAccount('123456', 1000, 500)
    assert account.account_number == '123456'
    assert account.balance == 1000
    assert account.overdraft_limit == 500

# Test case for depositing money
def test_deposit():
    account = CheckingAccount('123456', 1000, 500)
    account.deposit(500)
    assert account.balance == 1500

# Test case for withdrawing money within the overdraft limit
def test_withdraw_within_overdraft():
    account = CheckingAccount('123456', 1000, 500)
    account.withdraw(1500)
    assert account.balance == -500

# Test case for withdrawing money exceeding the overdraft limit
def test_withdraw_exceeding_overdraft():
    account = CheckingAccount('123456', 1000, 500)
    with pytest.raises(ValueError):
        account.withdraw(1600)

# Test case for getting transactions within a date range
def test_get_transactions():
    account = CheckingAccount('123456', 1000, 500)
    account.deposit(200, date=datetime.now() - timedelta(days=10))
    account.withdraw(100, date=datetime.now() - timedelta(days=5))
    start_date = datetime.now() - timedelta(days=30)
    end_date = datetime.now()
    transactions = account.get_transactions(start_date, end_date)
    assert len(transactions) == 2

# Test case for getting the total deposits last month
def test_get_total_deposits_last_month():
    account = CheckingAccount('123456', 1000, 500)
    account.deposit(300, date=datetime.now() - timedelta(days=15))
    account.deposit(200, date=datetime.now() - timedelta(days=10))
    total_deposits = account.get_total_deposits_last_month()
    assert total_deposits == 500

# Test case for getting the total withdrawals last month
def test_get_total_withdrawals_last_month():
    account = CheckingAccount('123456', 1000, 500)
    account.withdraw(100, date=datetime.now() - timedelta(days=20))
    account.withdraw(200, date=datetime.now() - timedelta(days=10))
    total_withdrawals = account.get_total_withdrawals_last_month()
    assert total_withdrawals == 300
