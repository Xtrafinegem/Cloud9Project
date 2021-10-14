#I created create an account interface#
print("\033[42m\033[30m******* WELCOME TO BANK OF CLOUD9*******")  # I change colour code from blue to black #
print("___________________________________________________________\n")
print("\033[34m \033[47m----------ACCOUNT CREATION----------")
name = input("Enter your name: ")
ID = int(input("Enter your National ID number: "))
Pass_Num = '1333'
account_number = '1406199220211007'
print("\033[32mCongratulations! Account created successfully......\n")
print(f"\033[30mYour secret code is: {Pass_Num} \n")

atm = ATM(name, account_number)
