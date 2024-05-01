from account import Account

class User:
    def __init__(self, name, email, address, account_type,bank):
        self.account = Account(name, email, address, account_type)
        self.bank = bank

    def create_account(self,bank):
        name = input("Enter name: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        account_type = input("Enter account type: ")
        self.account.account_number = self.bank.create_account(name, email, address, account_type)
        return self.account.account_number

    def deposit(self, bank, amount):
        bank.deposit(self.account.account_number, amount)

    def withdraw(self, bank, amount):
        if not bank.users[self.account.account_number].withdraw(amount):
            print("\n-----Withdraw amount exceeded")
        else:
            print(f"\n----- {amount} Taka Withdraw successfully!!! ------")

    def check_balance(self, bank):
        return bank.check_balance(self.account.account_number)
    
    def transaction_history(self):
        return self.bank.transaction_history(self.account.account_number)
    