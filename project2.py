import random
choose=["rock","papper","sicor"]
game=random.choice(choose)
chance=int(input("enter how many chance you like :"))
for i in range(chance):
    pick=input("enter your rock ,papper ,sicor :")
    if pick == game:
        print("draw ")
    elif pick == "rock" and game == "sicor":
        print("user won")
    elif pick == "rock" and game == "papper":
        print("bot won")
    elif pick=="papper" and game == "rock":
        print("user won")
    elif pick=="papper" and game == "sicor":
        print("bot won")
    elif pick =="sicor" and game =="papper":
        print("user won")
    elif pick =="sicor" and game =="rock":
        print("bot won")
    
