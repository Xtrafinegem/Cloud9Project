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
