import random

def player_damage(bot):
    print("which attack you want to land:")
    print('''1.punch
          2.kick
          3.main attack''')
    punch=10
    kick=12
    main_attack=24
    player_attack=int(input("enter your attack:"))
    if player_attack==1:
        bot=bot-punch
        print("player attack punch:")
        return bot
    
    elif player_attack==2:
       bot=bot-kick
       print("player attack kick")
       return bot
    
    elif player_attack ==3:
       bot=bot-main_attack
       print("  ulitmate smash  ")
       return bot
    
def bot_damage(player):
   a=random.randint(1,3)
   punch=10
   kick=12
   main_attack=23

   if a==1:
       print('Bot punch')
       player=player-punch
       return player
   
   if a==2:
       print(" bot kick ")
       player=player-kick
       return player
   
   if a==3:
       print(" bot ultimate attack ")
       player = player-main_attack
       return player
   
bot=100
player=100
while True:
  bot=player_damage(bot)
  print(f"hp of bot is{bot}")

  if bot<=0:
     print("bot got killed")
     print("                ")
     print("player won")
     break
     
  player=bot_damage(player)
  print(f"player hp is {player}")
  if player<=0:
    print("player died")
    print("           ")
    print(" bot won ")
    break
  
  print("      ")
  print("if you pick correct number you will heal")
  b=random.randint(1,5)
  pick=int(input("choose a number :"))

  if pick==b:
     player=player+10
  
  else:
     print("    ")
     print(f" the number was {b}")
     print("sorry wrong number ")

  print("    ")
  print("choose a number but if bot guessed it he will heal:")
  c=int(input("enter a number from (1-5)"))
  d=random.randint(1,4)
  print(f"bot picled {d}")
  if b==c:
     bot=bot+10
     print(bot)
  else:
     print("    ")
     print("bot wont get healing")
   



    