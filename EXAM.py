class Bank_Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.history = []
    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive")
        self.balance += amount
        self.history.append(f"Deposit {amount} UAH")
        print(f"\033[32mDeposit {amount} UAH")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive")
        self.balance -= amount
        self.history.append(f"\033[32mWithdraw {amount} UAH")
        print(f"\033[31mWithdraw {amount} UAH")
    def show_balance(self):
        print(f"\033[33mCurrent balance: {self.balance} UAH")
    def show_history(self):
        for i in self.history:
            print(operation)

aco = int(input("Money: "))
dep = int(input("Deposit: "))
wit = int(input("Withdraw: "))

account = Bank_Account("Ibrahim", aco)
account.show_balance()
account.deposit(dep)
account.show_balance()
account.withdraw(wit)
account.show_balance()