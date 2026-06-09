print('''1.cash balance
      2.Deposite money
      3.withdraw money
      4.Exit
      5.history''')
account = int(input("what is your current balance:"))
history=[]

while True:
    enter=int(input("what wouls you like to do:"))
    if enter==1:
        print("your account have balance of Rs ",account)

    elif enter == 2:
        deposit=float(input("enter the total amount of money you want to enter:"))
        account=account+deposit
        print(f"you have total of rs {account} in your account")
        history.append(f"Deposite is {deposit} and money left after deposite is {account}")
    elif enter == 3:
        withdraw=int(input("how much money you want to withdraw:"))
        if withdraw<account:
            account=account-withdraw
            print(f"you withdraw rs{withdraw} successfully")
            print(f"you have {account} left")
            history.append(f"withdrawn is {withdraw} and money left after withdrawn is {account}")
        else:
            print("you dont have enough money to withdraw:")
    elif enter ==4:
        exit=input("do you want exit :")
        if exit.lower()=="yes":
         break
        elif exit.lower()=="no":
            print("ok")
    elif enter==5:
        for transcation in history:
            print(transcation)

print(f"your current balance is: {account}")