# I added the withdraw function to the Clou9Bank source code.

def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("\033[31mInsufficient fund!")
            print(f"\033[34mYour balance is \033[32mGHC {self.balance} \033[34monly.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"\033[32mGHC {amount} withdrawal successful!")
            print("\033[34mCurrent account balance: \033[32mGHC", self.balance)
            print()
