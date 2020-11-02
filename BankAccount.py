import random

class BankAccount:
    # Class Attributes
    routing_number = 98765432
    def __init__(self, full_name):
        # Instance Attributes
        self.full_name = full_name
        self.account_number = random.randint(10000000, 99999999)
        self.balance = 0

    # Deposit Method
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${self.balance}")
