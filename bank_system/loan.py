class Loan:
    def __init__(self, customer, amount, interest_rate):
        self.customer = customer
        self.amount = amount
        self.interest_rate = interest_rate
        self.__remaining_balance = amount  # Initialize remaining balance to the total loan amount

    def calculate_interest(self):
        return self.__remaining_balance * self.interest_rate

    def make_payment(self, amount):
        if amount <= 0:
            raise ValueError("Invalid payment amount. Please enter a positive value.")

        if amount >= self.__remaining_balance:
            print("Congratulations! You have fully paid off your loan.")
            self.__remaining_balance = 0
        else:
            self.__remaining_balance -= amount
            print(f"Payment of {amount} made towards the loan. Remaining balance: {self.__remaining_balance}")

    @property
    def remaining_balance(self):
        return self.__remaining_balance
