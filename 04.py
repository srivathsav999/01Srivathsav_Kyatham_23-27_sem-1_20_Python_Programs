class Bank:
    def __init__(self):
        # Dictionary to store customer accounts and balances
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        """Create a new customer account with the given account number and initial balance."""
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            print(f"Account {account_number} created with an initial balance of ${initial_balance}.")
        else:
            print(f"Account {account_number} already exists. Please choose a different account number.")

    def get_balance(self, account_number):
        """Get the balance of a customer account."""
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print(f"Account {account_number} does not exist.")
            return None

    def deposit(self, account_number, amount):
        """Deposit money into a customer account."""
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"${amount} deposited into account {account_number}. New balance: ${self.accounts[account_number]}.")
        else:
            print(f"Account {account_number} does not exist.")

    def withdraw(self, account_number, amount):
        """Withdraw money from a customer account."""
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(f"${amount} withdrawn from account {account_number}. New balance: ${self.accounts[account_number]}.")
            else:
                print(f"Insufficient funds in account {account_number}.")
        else:
            print(f"Account {account_number} does not exist.")

# Example usage:
bank = Bank()

# Create accounts
bank.create_account("123456", initial_balance=1000)
bank.create_account("789012", initial_balance=500)

# Deposit and withdraw from accounts
bank.deposit("123456", 200)
bank.withdraw("789012", 100)

# Display balances
balance1 = bank.get_balance("123456")
balance2 = bank.get_balance("789012")

print(f"Account 123456 balance: ${balance1}")
print(f"Account 789012 balance: ${balance2}")
