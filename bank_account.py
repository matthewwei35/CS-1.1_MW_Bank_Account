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
        print(f"Amount Deposited: ${amount}")

    # Withdraw method
    def withdraw(self, amount):
        overdraft_fee = 10
        if amount > self.balance:
            self.balance -= overdraft_fee
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount}")

    # Get Balance Method
    def get_balance(self):
        print(f"Hello, your current balance is: ${round(self.balance, 2)}")

    # Add Interest Method
    def add_interest(self):
        monthly_interest = 0.00083
        interest = self.balance * monthly_interest
        self.balance += interest

    # Print Receipt Method
    def print_receipt(self):
        print(f"""{self.full_name}
Account No.: ****{str(self.account_number)[-4:]}
Routing No.: {self.routing_number}
Balance: ${round(self.balance, 2)}""")

# Instantiate objects
matthew = BankAccount("Matthew Wei")
thomas = BankAccount("Thomas Cat")
gerald = BankAccount("Gerald Mouse")

# Matthew
print("----------------------")

matthew.deposit(10)
matthew.withdraw(5)
matthew.get_balance()
matthew.add_interest()
matthew.print_receipt()

# Thomas
print("-----------------------")

thomas.deposit(20)
thomas.withdraw(30)
thomas.get_balance()
thomas.add_interest()
thomas.print_receipt()

# Gerald
print("----------------------")

gerald.deposit(100)
gerald.withdraw(99)
gerald.get_balance()
gerald.add_interest()
gerald.print_receipt()

# Divider
print("----------------------")