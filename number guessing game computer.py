import random

import os

clear = lambda: os.system("cls")

def n_guess():
    
    x = int(input("Select the upper value: "))
    C_choice = random.randint(0,x)
    print("The choosen number is: ", C_choice)
    game_on = True
    
    while game_on == True:
        result = input("Is the answer Too low(l), Too High(h), and It's right(r): ").lower()
        
        if result == "l":
            print("Too low")
            N_C_choice = random.randint(C_choice,x)
            print("The choosen number is: ", N_C_choice )
        elif result == "h":
            print("Too high")
            N_C_choice = random.randint(0,C_choice)
            print("The choosen number is: ", N_C_choice )
            game_on = False
        elif result == "r":
            print("The answer is right")
            
Should_continue = True

while Should_continue == True:
    
    n_guess()
    
    play_again = input("If you want to play again yes(y) or no(n): ").lower()
    
    
    
    if play_again == "y":
        clear()
    elif play_again == "n":
        print("Thanks for playing with me")
        Should_continue = False
    