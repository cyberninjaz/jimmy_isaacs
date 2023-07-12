import random
import enemy
encounters = ["zombie", "skeleton", "witch", "bandit", "nothing", "cave", "ruins", "canyon", "river"]
arrow = 0
burger = 0
name = input("What is your name?")
money = 20
stats = input("Pick a class: Fighter, Wizard, Archer, or Rogue")
if stats == "Fighter":
    health = 100
    max_health = 100
    magic = 0
    armor = 70
    attack = 70
    damage = 10
    ranged = 30
    stealth = 20
elif stats == "Wizard":
    health = 60
    max_health = 60
    magic = 90
    armor = 45
    attack = 50
    damage = 10
    ranged = 25
    stealth = 60
elif stats == "Archer":
    health = 75
    max_health = 75
    magic = 0
    armor = 85
    attack = 50
    damage = 10
    ranged = 95
    stealth = 60
    arrow = 20
elif stats == "Rogue":
    health = 60
    max_health = 60
    magic = 0
    armor = 45
    attack = 80
    damage = 10
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
                        print("Jake: Here are your arrows.")
                    else:
                        print ("Jake: You do not have enough money.")
                    if (item == "cheeseburger" or item == "Cheeseburger"):
                        if money >= 5:
                            burger += 1
                            money -= 5
                            print("Jake: Here is your cheseburger.")
                        else:
                            print("Jake: You do not have enough money.")
                    if (item == "blade sharpening" or item == "Blade Sharpening"):
                        if money >= 50:
                            attack += 10
                            money -= 50
                            ("Jake: Your blade has been sharpened.")
                        else:
                            print("Jake: You do not have enough money.")
                    if (item == "Armor Reinforcement" or item == "armor reinforcement"):
                        if money >= 70:
                            armor += 10
                            money -= 70
                            print("Jake: Your armor has been reinforced.")
                        else:
                            print("Jake: You do not have enough money.")
    action = input("What do you want to do this turn? You can rest or explore.")
    if (action == "rest" or action == "Rest"):
        if health + 20 <= max_health:
            health += 20
        else:
            health = max_health
        random.randint(0,100)
        if random.randint <= 30:
            money = money//2
            print("You got robbed in your sleep, you lost half your money.")
        else:
            print("You sleep peacefully.")
    elif (action == "explore" or action == "Explore"):
        random.choice(encounters)
    if random.choice == "zombie":
        ''
    if random.choice == "skeleton":
        ''
    if random.choice == "witch":
        ''
    if random.choice == "bandit":
        ''
    if random.choice == "nothing":
        ''
    if random.choice == "cave":
        ''
    if random.choice == "ruins":
        ''
    if random.choice == "canyon":
        ''
    if random.choice == "river":
        ''
