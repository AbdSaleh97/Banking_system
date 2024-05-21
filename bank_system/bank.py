from abc import ABC, abstractmethod
from bank_system.account import Account
from bank_system.customer import Customer

class BankingSystem(ABC):
    def __init__(self):
        self.__customers = {}
        self.__accounts = {}
        self.__customer_id = None

    def get_customers(self):
        return self.__customers

    def set_customers(self, customers):
        self.__customers = customers

    def get_accounts(self):
        return self.__accounts

    def set_accounts(self, accounts):
        self.__accounts = accounts

    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def add_customer(self, name):
        self.__customer_id = str(id(self))  # Using memory address as the customer ID
        if self.__customer_id not in self.__customers:
            customer = Customer(name)
            self.__customers[self.__customer_id] = customer
            self.__accounts[self.__customer_id] = []
            return customer
        else:
            print(f"Customer with ID {self.__customer_id} already exists.")
            return None

    def add_account(self, account_number, balance):
        if self.__customer_id in self.__customers:
            account = Account(account_number, balance)
            self.__accounts[self.__customer_id].append(account)
            return account
        else:
            print(f"Customer with ID {self.__customer_id} does not exist.")
            return None

    def delete_account(self, customer_id, account_number):
        if customer_id in self.__accounts:
            initial_len = len(self.__accounts[customer_id])
            self.__accounts[customer_id] = [account for account in self.__accounts[customer_id] if account.get_account_number() != account_number]
            if initial_len == len(self.__accounts[customer_id]):
                print(f"Account with number {account_number} does not exist for customer {customer_id}.")
            else:
                print(f"Account with number {account_number} deleted for customer {customer_id}.")
        else:
            print(f"Customer with ID {customer_id} does not exist.")

    def get_customer_accounts(self, customer_id):
        if customer_id in self.__accounts:
            return self.__accounts[customer_id]
        else:
            print(f"No accounts found for customer with ID {customer_id}")
            return None
        
    def delete_user(self, customer_id):
        if customer_id in self.__customers:
            # Deleting all accounts associated with the customer
            accounts_to_delete = self.__accounts.get(customer_id, [])
            for account in accounts_to_delete:
                self.delete_account(customer_id, account.get_account_number())

            # Now delete the customer
            del self.__customers[customer_id]
            del self.__accounts[customer_id]
            return "Customer deleted successfully with all associated accounts."
        else:
            return "Customer does not exist."
