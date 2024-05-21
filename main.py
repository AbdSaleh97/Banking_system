from bank_system.bank import BankingSystem

def display_menu():
    print("Welcome to the Banking System")
    print("1. Add Customer")
    print("2. Create Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Calculate Interest")
    print("6. Delete Account")
    print("7. Delete Customer")
    print("8. Exit")

def main():
    banking_system = BankingSystem()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter customer name: ")
            banking_system.add_customer(name)
            print("Customer added successfully!")
        
        elif choice == "2":
            customer_id = input("Enter customer ID: ")
            account_number = input("Enter account number: ")
            balance = float(input("Enter initial balance: "))
            banking_system.add_account(customer_id, account_number, balance)
            print("Account created successfully!")
        
        elif choice == "3":
            customer_id = input("Enter customer ID: ")
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            banking_system.deposit(customer_id, account_number, amount)
            print("Deposit successful!")
        
        elif choice == "4":
            customer_id = input("Enter customer ID: ")
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            banking_system.withdraw(customer_id, account_number, amount)
            print("Withdrawal successful!")
        
        elif choice == "5":
            customer_id = input("Enter customer ID: ")
            account_number = input("Enter account number: ")
            banking_system.calculate_interest(customer_id, account_number)
        
        elif choice == "6":
            customer_id = input("Enter customer ID: ")
            account_number = input("Enter account number: ")
            banking_system.delete_account(customer_id, account_number)
            print("Account deleted successfully!")
        
        elif choice == "7":
            customer_id = input("Enter customer ID: ")
            banking_system.delete_customer(customer_id)
            print("Customer deleted successfully!")
        
        elif choice == "8":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()
