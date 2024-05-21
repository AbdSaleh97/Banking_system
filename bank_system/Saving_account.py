from bank_system.account import Account

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self._Account__balance * self.interest_rate

    def deposit_interest(self):
        interest = self.calculate_interest()
        self.deposite(interest)

    def __str__(self):
        return f"Savings Account Number: {self._Account__account_number}, Balance: {self._Account__balance}"

