from .account import Account
from datetime import datetime, timedelta


class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
        self.transactions = []  # A list to keep track of all transactions

    def deposit(self, amount, date=datetime.now()):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(('deposit', amount, date))

    def withdraw(self, amount, date=datetime.now()):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            self.transactions.append(('withdrawal', amount, date))
        else:
            raise ValueError("Withdrawal amount exceeds overdraft limit.")

    def get_transactions(self, start_date, end_date):
        """Retrieve transactions between two dates."""
        return [t for t in self.transactions if start_date <= t[2] <= end_date]

    def get_last_month_transactions(self):
        """Retrieve last month's transactions."""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        return self.get_transactions(start_date, end_date)

    def get_total_deposits_last_month(self):
        """Calculate the total deposits from last month."""
        transactions = self.get_last_month_transactions()
        return sum(amount for t_type, amount, date in transactions if t_type == 'deposit')

    def get_total_withdrawals_last_month(self):
        """Calculate the total withdrawals from last month."""
        transactions = self.get_last_month_transactions()
        return sum(amount for t_type, amount, date in transactions if t_type == 'withdrawal')

    def __str__(self):
        return f"Checking Account Number: {self.account_number}, Balance: {self.balance}, Overdraft Limit: {self.overdraft_limit}"