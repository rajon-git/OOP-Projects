import random
from account import Account

class Bank:
    def __init__(self):
        self.users = {}
        self.loan_feature = True
        self.loan_amount = 0
        self.loan_cnt = 0

    def generate_account_number(self):
        return random.randint(10000, 99999)

    def create_account(self, name, email, address, account_type):
        account = Account(name, email, address, account_type)
        account_number = account.create_account()
        self.users[account_number] = account
        return account_number

    def delete_account(self, account_number):
        if account_number in self.users:
            del self.users[account_number]
            print("\n----- Account deleted successfully!!! -----")
        else:
            print("\n----- Account does not exist!!! -----")

    def show_users(self):
        if not self.users:
            print("\n----- No users found!!!------")
        else:
            for account_number, account in self.users.items():
                print(f"\n----- Account Number: {account_number}, Name: {account.name}, Email: {account.email}, Address: {account.address}, Account Type: {account.account_type}")

    def total_balance(self):
        total = sum(account.balance for account in self.users.values())
        print("\n----- Total balance:", total)

    def total_loan_amount(self):
        print("\n----- Total loan balance:", self.loan_amount)

    def toggle_loan_feature(self):
        self.loan_feature = not self.loan_feature
        if self.loan_feature:
            print("\n----- Loan feature is enabled now!!! -----")
        else:
            print("\n----- Loan feature is disabled now!!! -----")

    def deposit(self, account_number, amount):
        self.users[account_number].deposit(amount)

    def withdraw(self, account_number, amount):
        self.users[account_number].withdraw(amount)

    def check_balance(self, account_number):
        return self.users[account_number].balance

    def transaction_history(self, account_number):
        return self.users[account_number].transactions
        
    def take_loan(self, account_number, amount):
        account = self.users.get(account_number)
        if account:
            if self.loan_cnt < 2:
                self.loan_cnt += 1  
                self.loan_amount += amount
                print(f"\n----- Get total Loan: {amount}")
                return True
            else:
                print("\n----- Already taken maximum number of loans.!!! -----")
                return False
        else:
            print("\n----- Account not found.!!! -----")
            return False
