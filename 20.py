class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Insufficient funds.")
            return False


class Transaction:
    @staticmethod
    def verify_pin(account, entered_pin):
        return account.pin == entered_pin


class User:
    def __init__(self, name, accounts=[]):
        self.name = name
        self.accounts = accounts

    def add_account(self, account):
        self.accounts.append(account)


class ATM:
    @staticmethod
    def start_transaction(user, account_number, pin, amount=0):
        account = None
        for acc in user.accounts:
            if acc.account_number == account_number:
                account = acc
                break

        if account is not None and Transaction.verify_pin(account, pin):
            if amount > 0:
                if account.withdraw(amount):
                    print(f"Withdrawal successful. Remaining balance: {account.check_balance()}")
                else:
                    print("Withdrawal failed.")
            else:
                print(f"Current Balance: {account.check_balance()}")
        else:
            print("Invalid account number or PIN.")


# Example usage:

# Create accounts and users
account1 = Account(account_number="123456789", pin="1234", balance=1000)
account2 = Account(account_number="987654321", pin="4321", balance=2000)

user1 = User(name="John")
user1.add_account(account1)
user1.add_account(account2)

# Simulate ATM transactions
atm = ATM()

# Withdrawal
atm.start_transaction(user=user1, account_number="123456789", pin="1234", amount=500)

# Check balance
atm.start_transaction(user=user1, account_number="987654321", pin="4321")

# Incorrect PIN
atm.start_transaction(user=user1, account_number="123456789", pin="5678")
