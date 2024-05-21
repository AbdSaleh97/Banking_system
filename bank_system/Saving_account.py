from bank_system.account import Account

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        """Initialize a savings account with account number, balance, and interest rate."""
        super().__init__(account_number, balance)
        self.__interest_rate = interest_rate

    def deposit(self, amount):
        """Deposit money into the savings account."""
        if amount > 0:
            new_balance = self.get_balance() + amount
            self._set_balance(new_balance)

    def withdraw(self, amount):
        """Withdraw money from the savings account."""
        if 0 < amount <= self.get_balance():
            new_balance = self.get_balance() - amount
            self._set_balance(new_balance)
        else:
            raise ValueError("Insufficient funds")

    def calculate_interest(self):
        """Calculate the interest on the current balance."""
        return self.get_balance() * self.__interest_rate

    def deposit_interest(self):
        """Deposit the calculated interest into the savings account."""
        interest = self.calculate_interest()
        self.deposit(interest)

    def get_interest_rate(self):
        """Get the interest rate of the savings account."""
        return self.__interest_rate

    def __str__(self):
        """Return a string representation of the savings account."""
        return f"Savings Account Number: {self.get_account_number()}, Balance: {self.get_balance()}, Interest Rate: {self.__interest_rate}"
