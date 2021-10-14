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
                    ***
                        Menu:
                        1. 3 months - 12.60%
                        2. 6 months - 12.90%
                        3. 1 year   - 14.00%
                    ***
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
                **************
                    Transaction is now complete.                         
                    Transaction number: {random.randint(10000, 1000000)} 
                    Account holder: {self.name.upper()}                  
                    Account number: {self.account_number}                
                    Available balance: GHC {self.balance}                    
                    \033[3mThanks for choosing us as your bank                  
                **************
                """)
                sys.exit()
