import random
options = ["rock", "paper", "scissors"]
player_one = 0
cpu = 0
while True:
    messi = (input("player one pick rock, paper, or scissors."))
    ronaldo = random.choice(options)
    if messi == ronaldo:
        print ("tie")
    if (messi == "rock" or messi == "Rock") and (ronaldo == "scissors" or ronaldo == "Scissors"):
        print ("player one wins")
        player_one += 1
    if (messi == "rock" or messi == "Rock") and (ronaldo == "paper" or ronaldo == "Paper"):
        print ("cpu wins")
        cpu += 1
    if (messi == "paper" or messi == "Paper") and (ronaldo == "rock" or ronaldo == "Rock"):
        print ("player one wins")
        player_one += 1
    if (messi == "paper" or messi == "Paper") and (ronaldo == "scissors" or ronaldo =="Scissors"):
        print ("cpu wins")
        cpu += 1
    if (messi == "scissors" or messi == "Scissors") and (ronaldo == "paper" or ronaldo == "Paper"):
        print ("player one wins")
        player_one += 1
    if (messi == "scissors" or messi == "Scissors") and (ronaldo == "rock" or ronaldo == "Rock"):
        print ("cpu wins")
    print ("player one picked", messi)
    print ("cpu picked", ronaldo)
    print ("player one score:", player_one)
    print ("cpu score", cpu)
    mbappe = (input("do you want to play again"))
    print("\n----------------------------------------------")
    if mbappe == "no":
        break