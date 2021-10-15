# I added the transfer function to the Cloud9 ATM source code
def transfer(self,trans_amount):
        if trans_amount > self.balance:
            print("\033[31mInsufficient fund!")
            print(f"\033[34mYour balance is \033[32mGHC {self.balance} \033[34monly.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - trans_amount
            print(f"\033[32mGHC {trans_amount} Transfer successful!")
            print("\033[34mCurrent account balance: \033[32mGHC", self.balance)
            print()        

    def check_balance(self):
        print("\033[34mAvailable balance: \033[32mGHC", self.balance)
        print()
