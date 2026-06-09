import random

choose = ["rock", "paper", "scissor"]

chance = int(input("enter your chance :"))

p = 0
q = 0

for i in range(chance):

    user = input("enter your rock, paper, scissor : ").lower()
    bot = random.choice(choose)

    print(f"bot chose {bot}")

    if user == bot:
        print("draw")

    elif user == "rock" and bot == "scissor":
        print("user won")
        p += 1

    elif user == "rock" and bot == "paper":
        print("bot won")
        q += 1

    elif user == "paper" and bot == "rock":
        print("user won")
        p += 1

    elif user == "paper" and bot == "scissor":
        print("bot won")
        q += 1

    elif user == "scissor" and bot == "rock":
        print("bot won")
        q += 1

    elif user == "scissor" and bot == "paper":
        print("user won")
        p += 1

    else:
        print("invalid input")

if p > q:
    print(f"user won most rounds which is {p} and bot only won {q}")

elif q > p:
    print(f"bot won by {q} rounds and user won by {p} rounds")

else:
    print(f"game draw, both won {p} rounds")