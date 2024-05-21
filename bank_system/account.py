from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self, account_number, balance=0.0):
        self.__account_number = account_number
        self.__balance = balance

    def deposite(self, amount):
        self.__balance += amount
        print("Deposit of", amount, "was added to your account")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def transfer(self, to_account, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            to_account.__balance += amount
        else:
            print("Insufficient funds")

    def __str__(self):
        return f"Checking Account Number: {self.__account_number}, Balance: {self.__balance}"



