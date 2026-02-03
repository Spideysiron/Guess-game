balance = 1000

def check_balance(balance):
    print(f"Your balance: {balance}")
    return balance


def deposit(balance):
    depo = input("How much money you want to deposit? : ")
    if depo.isdigit():
        balance += int(depo)
        print(f"Your money is depodited succesfully! \n Your Available balance is {balance}")

    else:
        print("enter a valid amount.")
    
    return balance


def withdraw(balance):
    wdraw = input("How much money you want to withdraw?: ")
    if wdraw.isdigit():
        wdraw = int(wdraw)
        if wdraw > balance:
            print("Insufficient funds!!")
        else:
            balance -= wdraw
            print(f"Your money withdrawed succesfully! \n Your Available balance is {balance}")
            

    else:
        print("enter a valid amount.")
    return balance



while True:
    menu = input("what would you like to do? \n 1. Check Balance \n 2. Deposit \n 3. Withdraw \n 4. Exit \n Choose an option(1 to 4): ").strip()

    if menu.isdigit():
        menu = int(menu)
        
        if menu == 1:
            balance = check_balance(balance)

        elif menu == 2:
            balance = deposit(balance)
        
        elif menu == 3:
            balance = withdraw(balance)
            
        elif menu == 4:
            print("Thank you for visiting the ATM!")
            break

    else:
        print("enter a valid operation(1-4).")