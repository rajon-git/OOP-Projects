import random

class Account:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = None
        self.transactions = []

    def generate_account_number(self):
        return random.randint(10000, 99999)

    def create_account(self):
        self.account_number = self.generate_account_number()
        return self.account_number

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"\n----- Deposited Balance: {amount} taka")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"\n----- Withdraw Balance: {amount} taka")
            return True
        else:
            return False
