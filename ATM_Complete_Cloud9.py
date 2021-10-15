import random
import sys

class ATM():
    def __init__(self, name, account_number, balance = 0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    
    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"\033[34mAvailable balance: \033[32mGHC {self.balance}\n")
        
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("\033[34mCurrent account balance: \033[32mGHC", self.balance)
        print()

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


   
    def transaction(self):
            print("Hello " + self.name)
            print("What would you like to do today?")
            print("""
                \033[32mTRANSACTION 
            *********************
                Menu:
                1. Account Detail
                2. Check Balance
                3. Deposit
                4. Withdraw
                5. Transfer
                6. Investment
                7. Print Receipt/Exit
            *********************
            """)
            while True:
                try:
                    option = int(input("\033[34mEnter 1, 2, 3, 4, 5, 6 or 7: "))
                except:
                    print("\033[31mError: Enter 1, 2, 3, 4, 5, 6 or 7 only!\n")
                    continue
                else:
                    
                    if option == 1:
                        passcode = str(input("Enter passcode: "));
                        if passcode != Pass_Num:
                            print("\033[31minvalid password try again")
                            return option
                        else:
                    
                            atm.account_detail()
                            return option
                            
                    
                    elif option == 2:
                        passcode = str(input("Enter passcode: "))
                        if passcode != Pass_Num:
                            print("\033[31minvalid try again")
                        else:
                            atm.check_balance()
                            return option
                    
                    elif option == 3:
                        amount = float(input("How much do you want to deposit(GHC)?: "))
                        Do = str(input("Put amount in the tray on your left side. If Done enter(y/n): "));
                        if Do == 'y':
                            passcode = str(input("Enter passcode: "))
                        if passcode != Pass_Num:
                            print("\033[31minvalid try again")
                            return option
                        else:
                            print("\033[32mDeposit Successful")
                            atm.deposit(amount)
                            return option
                    
                    elif option == 4:
                        amount = float(input("How much do you want to withdraw?(GHC):"))
                        passcode = str(input("Enter passcode: "))
                        if passcode != Pass_Num:
                            print("\033[31minvalid try again")
                            return option
                        else:
                            atm.withdraw(amount)
                            return option
                    
                    elif option == 5:
                        trans_amount = float(input("please input amount to be transfered(GHC): "))
                        lname = input("please enter receiver surname: ")
                        receiver_account_no = int(input("please input receiver account number: "))
                        passcode = str(input("Enter passcode: "))
                        if passcode != Pass_Num:
                            print("\033[31minvalid try again")
                            return option
                        else:
                            atm.transfer(trans_amount)
                            return option

                    elif option == 6:
                        print("""\033[32m
                        TREASURY BILL
                    *******
                        Menu:
                        1. 3 months - 12.60%
                        2. 6 months - 12.90%
                        3. 1 year   - 14.00%
                    *******
                    """)
                        passcode = str(input("\033[34mEnter passcode: "))
                        if passcode != Pass_Num:
                            print("\033[31minvalid try again")
                            return option
                        else:
                            atm.investments()
                            return option 

                    elif option == 7:
                            print(f"""
                        \033[46m \033[30mprinting receipt..............
                ******************************************
                    Transaction is now complete.                         
                    Transaction number: {random.randint(10000, 1000000)} 
                    Account holder: {self.name.upper()}                  
                    Account number: {self.account_number}                
                    Available balance: GHC {self.balance}                    

                    \033[3mThanks for choosing us as your bank                  
                ******************************************
                """)
                    else: 
                        print("Error! Choose 1,2,3,4,5,6 or 7 only")
                        return option
                sys.exit()


    def investments(self):
       
        while True:
            try:
                    option = int(input("Enter 1, 2, or 3:"))
            except:
                    print("Error: Enter 1, 2, or 3: only!\n")
                    continue
            else:
                print("How much are you willing to invest?")
                invAmount = int(input())
                self.balance = self.balance
                if invAmount > self.balance:
                    print("\033[31mInsufficient fund!")
                    print(f"\033[34mYour balance is \033[32mGHC {self.balance} \033[34monly.")
                    print("Please choose option 3 and make a deposit.")
                    print()
                    return
            
                else:
                    intAmt =str(invAmount * 0.129)
                    self.balance = self.balance - invAmount
                    if option == 1:
                        
                        print("You will receive " + intAmt + " as interest after the period")
                        print(f"\033[32mGHC {invAmount} Invested successfully!")
                        print("\033[34mCurrent account balance: \033[32mGHC", self.balance)
                        print()
                    
                    elif option == 2:
                        intAmt =str(invAmount * 0.126)
                        self.balance == self.balance - invAmount
                        print("You will receive " + intAmt + " as interest after the period")
                        print(f"\033[32mGHC {invAmount} Invested successfully!")
                        print("\033[34mCurrent account balance: \033[32mGHC", self.balance)
                        print()
                    elif option == 3:
                        intAmt =str(invAmount * 0.14)
                        self.balance == self.balance - invAmount
                        print("You will receive " + intAmt + " as interest after the period")
                        print(f"\033[32mGHC {invAmount} Invested successfully!")
                        print("\033[34mCurrent account balance: \033[32mGHC", self.balance)
                        print()
                    else:
                        print("Wrong command!")
                    break
            
                

print("\033[42m\033[30m******* WELCOME TO BANK OF CLOUD9*******") ##I changed the font color from blue to black.
print("___________________________________________________________\n")
print("\033[34m \033[47m----------ACCOUNT CREATION----------")
name = input("Enter your name: ")
ID = int(input("Enter your National ID number: "))
Pass_Num = '1333'
account_number = '1406199220211007'
print("\033[32mCongratulations! Account created successfully......\n")
print(f"\033[30mYour secret code is: {Pass_Num} \n")

atm = ATM(name, account_number)

while True:
    trans = input("\033[34mDo you want to do any transaction?(y/n):")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("""\033[32m \033[3m
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
        """)
        break
    else:
        print("\033[31mWrong command!  Enter 'y' for yes and 'n' for NO.\n")
