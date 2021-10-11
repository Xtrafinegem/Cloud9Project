 def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("\033[34mCurrent account balance: \033[32mGHC", self.balance)
        print()
