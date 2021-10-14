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
