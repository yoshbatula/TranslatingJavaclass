class Transaction:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("You can't deposit a negative or zero amount.")
        else:
            self.balance += amount
            print(f"Succesfully deposited: ${amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            self.balance -= amount
            print(f"Succesfully withdraw: ${amount}")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")