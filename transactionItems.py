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
                        amount = float(input("How much do you want to deposit(GHC): "))
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
                        amount = float(input("How much do you want to withdraw(GHC):"))
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
                        \033[46m \033[34mprinting receipt..............
                ******************************************
                    Transaction is now complete.                         
                    Transaction number: {random.randint(10000, 1000000)} 
                    Account holder: {self.name.upper()}                  
                    Account number: {self.account_number}                
                    Available balance: GHC {self.balance}                    

                    \033[3mThanks for choosing us as your bank                  
                ******************************************
                """)
                sys.exit()
