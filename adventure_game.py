import random
import enemy
success = 0
encounters = ["zombie", "skeleton", "witch", "bandit", "nothing", "cave", "ruins", "canyon", "river"]
arrow = 0
burger = 0
name = input("What is your name? ")
money = 20
stats = input("Pick a class: Fighter, Wizard, Archer, or Rogue: ").upper()
if stats == "FIGHTER":
    health = 100
    max_health = 100
    magic = 0
    armor = 70
    attack = 70
    damage = 10
    ranged = 30
    stealth = 20
elif stats == "WIZARD":
    health = 60
    max_health = 60
    magic = 90
    armor = 45
    attack = 50
    damage = 10
    ranged = 25
    stealth = 60
elif stats == "ARCHER":
    health = 75
    max_health = 75
    magic = 0
    armor = 75
    attack = 50
    damage = 10
    ranged = 95
    stealth = 60
    arrow = 20
elif stats == "ROGUE":
    health = 60
    max_health = 60
    magic = 0
    armor = 45
    attack = 80
    damage = 10
    ranged = 25
    steath = 90
def combat(mob, money):
    y = random.randint(1,5)
    enemies = []
    if mob == "zombie":
        print(f'you find {y} zombies')
        for num in range(y):
            enemies.append(enemy.zombie(15,40,30,20))
    elif mob == "skeleton":
        print(f'you find {y} skeletons')
        for num in range(y):
            enemies.append(enemy.zombie(20,50,20,15))
    elif mob == "witch":
        print(f'you find {y} witches')
        for num in range(y):
            enemies.append(enemy.zombie(30,55,10,30))
    elif mob == "bandit":
        print("A Bandit appears but nothing happens yet (WIP)")
    elif mob == "nothing":
        print ("You find nothing.")
    elif mob == "cave":
        cave = input("You found a cave do you want to explore it? ")
        if (cave == "yes" or cave == "Yes"):
            print("You found spiders in the cave.")
            for num in range(y):
                enemies.append(enemy.zombie(10,50,10,10))
    elif mob == "ruins":
        riddles = ["I have a golden head. I have a golden tail. I have no body. I am a...", "I have two hands on my face but no arms. I am a...", "Many have heard me, yet nobody has seen me. I won't speak back unless spoken to. I am a...", "What five long word become shorter when you add two letters?..."]
        answers = ["GOLDEN COIN", "CLOCK", "ECHO", "SHORT"]
        m = random.randint(15,40)
        ruins = input("You found ruins, do you want to explore the ruins? ")
        if (ruins == "yes" or ruins == "Yes"):
            j = random.randint(0,3)
            print(f"Answer this riddle for a prize: {riddles[j]}")
            answer = input("Answer: ")
            answer = answer.upper()
            if answer == answers[j]:
                print(f"Correct, you got {m} coins.")
                return money + m
    elif mob == "canyon":
        canyon = input("You run into a canyon, you have to find a way through.\nThere are two options: \na.) There is a guy in front of a bridge which you could talk to \nb.) You could try to find a way on your own.\nA or B: ")
        if canyon == "a":
            man = input("You talk to the man, he tells you that if you pay him 20 coins he will let you use his bridge.\nDo you want to pay him? ")
            if (man == "yes" or man == "Yes"):
                print("You use the bridge, you are now across.")
                return money - 20
            else:
                print("You don't use the bridge.")
        else:
            print("You do not use the bridge.") 
    elif mob == "river":
        river = input("You run into a river, you have to find a way through.\nThere are two options:\na.) There is a guy in front of a bridge which you could talk to\nb.) You could try to find a way on your own.\nA or B: ")
        if river == "a":
            man = input("You talk to the man, he tells you that if you pay him 20 coins he will let you use his bridge.\nDo you want to pay him? ")
            if (man == "yes" or man == "Yes"):
                print("You use the bridge, you are now across.")
                return money - 20
            else:
                print("You don't use the bridge.")
        else:
            print("You do not use the bridge.")
    return 'no'
while True:
    if burger > 0:
        if input(f"Do you want to eat cheeseburger? You have {burger} cheeseburger(s) left. ").upper() == "YES":
            health += 10
    if random.randint(0,100) <= 20:
        trader = input("Jake showed up, do you buy from him? ")
        if (trader == "Yes" or trader == "yes"):
            while True:
                print(f"You have {money} coins")
                item = input("Jake: What do you want to buy? You can buy: \n $5 10 arrows \n $5 cheeseburger \n $50 blade sharpening \n $70 armor reinforement \n ").upper()
                if (item == "ARROWS"):
                    if money >= 5:
                        arrow += 10
                        money -= 5
                        print("Jake: Here are your arrows.")
                    else:
                        print ("Jake: You do not have enough money.")
                elif (item == "CHEESEBURGER"):
                    if money >= 5:
                        burger += 1
                        money -= 5
                        print("Jake: Here is your cheseburger.")
                    else:
                        print("Jake: You do not have enough money.")
                elif (item == "BLADE SHARPENING"):
                    if money >= 50:
                        attack += 10
                        money -= 50
                        ("Jake: Your blade has been sharpened.")
                    else:
                        print("Jake: You do not have enough money.")
                elif (item == "ARMOR REINFORCEMENT"):
                    if money >= 70:
                        armor += 10
                        money -= 70
                        print("Jake: Your armor has been reinforced.")
                    else:
                        print("Jake: You do not have enough money.")
                ask = input("Do you want to buy from the trader again?").upper()
                if ask == 'NO':
                    break

    action = input("What do you want to do this turn? You can rest or explore: ").upper()
    if action == "REST":
        if health + 20 <= max_health:
            health += 20
        else:
            health = max_health
        x = random.randint(0,100)
        if x <= 30:
            money = money//2
            print(f"You got robbed in your sleep, you lost half your coins. You have {money} coins left")
        else:
            print("You slept peacefully.")
    elif action == "EXPLORE":
        encounter = random.choice(encounters)
        check = combat(encounter, money)
        if type(check) == int:
            money = check
        success += 1
        if success >= 5:
            print("You win!")
            break
    print("\n------------End of Day------------\n")
