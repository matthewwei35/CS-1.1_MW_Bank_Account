import random

class BankAccount:
    """
    A class to respresent a bank account.

    Attributes
    ----------
    full_name : str
        the first and last name of the bank account owner
    account_number : int
        randomly generated 8 digit number, unique per account
    routing_number : int
        9 digit number, this number is the same for all accounts
    balance : int
        the balance of money in the account, it should start at 0

    Methods
    -------
    def deposit(amount):
        take one parameter amount and will add amount to the balance, also will print a confirmati-
        on message with amount deposited
    def withdraw(amount):
        take one parameter amount and will subtract amount from the balance, also will print a con-
        firmation message with the amount withdrawn
    def get_balance():
        print a user-friendly message with the account balance, also will return the current balan-
        ce of the account
    def add_interest():
        adds interest to the user's balance
    def print_receipt():
        prints a receipt with the account name, account number, routing number, and balance
    """

    routing_number = 987654323
    def __init__(self, full_name):
        """
        Constructs necessary attributes for the BankAccount object.

        Parameters
        ----------
        full_name : str
            the first and last name of the bank account owner
        """

        self.full_name = full_name
        self.account_number = random.randint(10000000, 99999999)
        self.balance = 0

    # Deposit Method
    def deposit(self, amount):
        """
        Takes one parameter amount and will subtract amount from the balance, also will print a co-
        nfirmation message with amount withdrawn.

        Parameters
        ----------
        amount : int
            the value that is being added to the balance
        """
        self.balance += amount
        print(f"Amount Deposited: ${amount}")

    # Withdraw method
    def withdraw(self, amount):
        """
        Takes one parameter amount and will add amount to the balance, also will print a confirmat-
        ion message with amount deposited. If the user tries to withdraw an amount that is greater/
        larger than the current balance, print ”Insufficient funds.” and charge them with an overd-
        raft fee.

        Parameters
        ----------
        amount : int
            the value that is being subtracted from the balance
        """
        overdraft_fee = 10
        if amount > self.balance:
            self.balance -= overdraft_fee
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount}")

    # Get Balance Method
    def get_balance(self):
        """
        Will print a user-friendly message with the account balance and then also return the curre-
        nt balance of the account.

        Parameters
        ----------
        None
        """
        print(f"Hello, your current balance is: ${round(self.balance, 2)}")

    # Add Interest Method
    def add_interest(self):
        """
        Adds interest to the user's current balance. The annual interest rate is 1% (i.e. 0.083% p-
        er month). The monthly interest is calculated by the following equation: interest = balanc-
        e * 0.00083.

        Parameters
        ----------
        None
        """
        monthly_interest = 0.00083
        interest = self.balance * monthly_interest
        self.balance += interest

    # Print Receipt Method
    def print_receipt(self):
        """
        Prints a receipt with the account name, account number, routing number, and balance.

        Parameters
        ----------
        None
        """
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
