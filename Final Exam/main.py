from bank import Bank
from admin import Admin
from user import User

bank = Bank()
admin = Admin(bank)
user = User("Rajon", "rajon@gmail.com", "Dhaka", "Savings",bank)

while True:
    print("\n ------ Welcome To My Bank Dashboard -----")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        while True:
            print("\n ----- Welcome To My Bank -----")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Transaction History")
            print("6. Take Loan")
            print("7. Exit")

            customer_choice = int(input("Enter your choice: "))

            if customer_choice == 1:
                user.create_account(bank)
                print(f"\n----- Account created successfully! Your account number is: {user.account.account_number}")
            elif customer_choice == 2:
                amount = int(input("Enter the amount to deposit: "))
                user.deposit(bank, amount)
                print(f"\n----- {amount} Taka deposited successfully!!! ------")
            elif customer_choice == 3:
                amount = int(input("Enter the amount to withdraw: "))
                user.withdraw(bank, amount)
            elif customer_choice == 4:
                balance = user.check_balance(bank)
                print(f"\n-----Available balance: {balance}")

            elif customer_choice == 5:
                history = user.transaction_history()
                if history:
                    print("\n----- Transaction History: ------")
                    for transaction in history:
                        print(transaction)
                else:
                    print("\n-----No transactions found!!!.-----")
            
            elif customer_choice == 6:
                account_number = user.account.account_number 
                amount = int(input("Enter the loan amount: "))
                bank.take_loan(account_number, amount)

            elif customer_choice == 7:
                break

            else:
                print("-----Invalid choice!!!-----")
        
    elif choice == 2:
        while True:
            print("\n----- Welcome Admin -----")
            print("1. Create Account")
            print("2. Delete Account")
            print("3. Show All Accounts")
            print("4. Total Balance")
            print("5. Total Loan Amount")
            print("6. Loan Enable or Disable")
            print("7. Exit")
            admin_choice = int(input("Enter your choice: "))
            if admin_choice == 1:
                admin.create_account()
            elif admin_choice == 2:
                admin.delete_account()
            elif admin_choice == 3:
                admin.show_all_accounts()
            elif admin_choice == 4:
                admin.total_balance()
            elif admin_choice == 5:
                admin.total_loan_amount()
            elif admin_choice == 6:
                admin.toggle_loan_feature()
            elif admin_choice == 7:
                break
            else:
                print("-----Invalid choice!!!-----")
    elif choice == 3:
        break
    else:
        print("-----Invalid choice!!!-----")
