import random
arrow = 0
burger = 0
name = input("What is your name?")
money = 20.00
stats = input("Pick a class: Fighter, Wizard, Archer, or Rogue")
if stats == "Fighter":
    health = 100
    magic = 0
    armor = 70
    attack = 70
    ranged = 30
    stealth = 20
elif stats == "Wizard":
    health = 60
    magic = 90
    armor = 45
    attack = 50
    ranged = 25
    stealth = 60
elif stats == "Archer":
    health = 75
    magic = 0
    armor = 85
    attack = 50
    ranged = 95
    stealth = 60
    arrow = 20
elif stats == "Rogue":
    health = 60
    magic = 0
    armor = 45
    attack = 80
    ranged = 25
    steath = 90

    
while True:
    if burger > 0:
        if input(f"Do you want to eat cheeseburger? You have {burger} cheeseburger(s) left") == "yes":
            health += 10
    if random.randint(0,100) <= 20:
        trader = input("Jake showed up, do you buy from him?")
        if (trader == "Yes" or trader == "yes"):
            while True:
                item = input("Jake: What do you want to buy? You can buy: \n $5 10 arrows \n $5 cheeseburger \n $50 blade sharpening \n $70 armor reinforement \n ")
                if (item == "arrows" or item == "Arrows"):
                    if money >= 5:
                        arrow += 10
                        money -= 5
                    else:
                        print ("Jake: You do not have enough money.")
                    if (item == "cheeseburger" or item == "Cheeseburger"):
                        if money >= 5:
                            burger += 1
                            money -= 5
                        else:
                            print("Jake: You do not have enough money.")
                        
    action = input("What do you want to do this turn? You can rest, explore, or build.")
    if (action == "rest" or action == "Rest"):
        ''
