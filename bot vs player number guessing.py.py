import random
def bot():
    a=random.randint(1,10)
    print("if bot pick correct number you loos")
    pick=int(input("enter a number to choose "))
    print(f"bot choosed {a} ")
    if a == pick:
        print("bot won the match:")
        quit()
    else:
        print("bot choosed wrong number :")

def player():
    b=random.randint(1,10)
    print("if you pick correct answer you won:")
    choose=int(input("choose a number :"))
    print(f"bot picked {b}")
    if choose == b:
        print("player won the game :")
        quit()
    else :
        print("player choosed wrong numder :")

while True:
    bot()
    player()
