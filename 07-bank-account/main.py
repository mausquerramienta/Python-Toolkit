# Bank Account

import os

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Client(Person):
    def __init__(self, first_name, last_name, account_number):
        super().__init__(first_name, last_name)
        self.account_number = account_number
        self.balance = 0.0

    def __str__(self):
        return f"Account Holder: {self.first_name.upper()} {self.last_name.upper()}\nAccount Number: {self.account_number}\nAvailable Balance: ${self.balance:,.2f}"

    def deposit(self, amount):
        print(f"Amount to deposit: ${amount:,.2f}")
        self.balance += amount
        print("Deposit processed successfully.")
        print(f"New Balance: ${self.balance:,.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            print(f"Your available balance is only ${self.balance:,.2f}.")
            return False
        else:
            print(f"Amount to withdraw: ${amount:,.2f}")
            self.balance -= amount
            print("Withdrawal processed successfully.")
            print(f"Remaining Balance: ${self.balance:,.2f}")
            return True

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def create_client():
    print("ACCOUNT REGISTRATION")
    print("-" * 50)
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    account_number = input("Create an account number: ")
    print("\nBank account created successfully.")
    return Client(first_name, last_name, account_number)

def request_amount(action):
    while True:
        amount = input(f"Enter the amount to {action}: $")        
        if amount.replace(".", "", 1).isnumeric():
            amount = float(amount)
            if amount > 0:
                return amount
            else:
                print("⚠️ The amount must be greater than $0.00.")
        else:
            print("Invalid input. Please enter a valid number.")

def start_program():
    clear_screen()
    print("=" * 50)
    print("Welcome to MAUSQUERRAMIENTA CENTRAL BANK")
    print("=" * 50)
    print("To get started, you need to open an account.\n")
    
    my_client = create_client()
    
    print("=" * 50)
    input("Press ENTER to continue...")
    
    while True:
        clear_screen()
        print("=" * 50)
        print("MAIN MENU")
        print("=" * 50)
        print("[1] Account Statement")
        print("[2] Deposit Funds")
        print("[3] Withdraw Funds")
        print("[4] Log Out")
        print("-" * 50)
        
        choice = input("Select an operation number (1-4): ")
        
        if choice.isnumeric() and int(choice) in range(1, 5):
            choice = int(choice)
            clear_screen()
            
            match choice:
                case 1:
                    print("=" * 50)
                    print("ACCOUNT STATEMENT")
                    print("=" * 50)
                    print(my_client)
                    print("=" * 50)
                case 2:
                    print("=" * 50)
                    print("DEPOSIT MODULE")
                    print("=" * 50)
                    amount = request_amount("deposit")
                    print("-" * 50)
                    my_client.deposit(amount)
                    print("=" * 50)
                case 3:
                    print("=" * 50)
                    print("WITHDRAWAL MODULE")
                    print("=" * 50)
                    if my_client.balance == 0:
                        print("⚠️ You have $0.00 in your account.")
                        print("Please deposit funds before making a withdrawal.")
                        print("=" * 50)
                    else:
                        while True:
                            amount = request_amount("withdraw")
                            print("-" * 50)
                            if my_client.withdraw(amount):
                                print("=" * 50)
                                break
                            print("\nLet's try again.")
                case 4:
                    print("=" * 50)
                    print("Logging out...")
                    print("Thank you for choosing Mausquerramienta Central Bank.")
                    print("Have a great day!")
                    print("=" * 50)
                    break
        else:
            print("\nInvalid option. Please select a valid number from the menu.")
            
        input("\nPress ENTER to continue...")

start_program()
