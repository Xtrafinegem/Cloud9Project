 def transaction(self):
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
                        amount = float(input("How much do you want to deposit?(GHC): "))
                        Do = str(input("Put amount on the tray on your left side. If Done enter(y/n): "));
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
                    
                   
                     
