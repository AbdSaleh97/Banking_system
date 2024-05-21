from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance):
        """Initialize an account with an account number and balance."""
        self.__account_number = account_number
        self.__balance = balance

    @abstractmethod
    def deposit(self, amount):
        """Deposit money into the account."""
        pass

    @abstractmethod
    def withdraw(self, amount):
        """Withdraw money from the account."""
        pass

    def transfer(self, to_account, amount):
        """Transfer money to another account."""
        if self.__balance >= amount:
            self.withdraw(amount)
            to_account.deposit(amount)
        else:
            raise ValueError("Insufficient funds")

    def get_account_number(self):
        """Get the account number."""
        return self.__account_number

    def get_balance(self):
        """Get the account balance."""
        return self.__balance

    def _set_balance(self, amount):
        """Set the account balance."""
        self.__balance = amount

    def __str__(self):
        """Return a string representation of the account."""
        return f"Checking Account Number: {self.__account_number}, Balance: {self.__balance}"
