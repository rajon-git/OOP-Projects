class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self):
        name = input("Enter name: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        account_type = input("Enter account type: ")
        self.bank.create_account(name, email, address, account_type)

    def delete_account(self):
        account_number = int(input("\nEnter account number to delete: "))
        self.bank.delete_account(account_number)

    def show_all_accounts(self):
        self.bank.show_users()

    def total_balance(self):
        self.bank.total_balance()

    def total_loan_amount(self):
        self.bank.total_loan_amount()

    def toggle_loan_feature(self):
        self.bank.toggle_loan_feature()

