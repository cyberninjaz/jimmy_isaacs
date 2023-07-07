import random
option = ["lives","fire","weather","function","python","paper","meatball","zodiac","electrons","posotive","negative","digit","program","science","writing","analysis","does","major","leaving","biodiversity","scout","animal","school","park","mined","copied","france","world","ocean","starfish","comma","doctor","work","physician","physical","property","laws","path","ownership","drum","period","spanish","finish"]
def pick(option):
    return random.choice(option)
while True:
    word = pick(option)
    print("the word has", len(word), "lettersm")
    counter1 = 9
    while True:
        counter = 1
        
        check = False
        player = input("Pick a letter")
        for ch in word:
            if ch == player:
                check = True
                if counter == 1:
                    print (player, "is in the 1st spot")
                elif counter == 2:
                    print (player, "is in the 2nd spot")
                elif counter == 3:
                    print (player, "is in the 3rd spot")
                else:
                    print (player, "is in the", counter, "th spot")
            counter += 1
        if check == False:
            print(player, "is not in the word")
            counter1 -= 1
            print("You have", counter1, "lives left.")
        if counter1 == 0:
            print("you lose")
            break
        guess = input("Do you want to guess a word?")
        if (guess == "yes" or guess == "Yes"):
            worda = input("What is the word?")
            if worda == word:
                print ("You win")
                break
    play_again = input("Do you want to play again?")
    if (play_again == "no" or play_again == "No"):
        break