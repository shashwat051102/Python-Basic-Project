import random

import os

clear = lambda: os.system("cls")


dice = [1, 2, 3, 4, 5, 6]

N_players = int(input("Number of players playing: "))


def game():
    N_games = int(input("NUmber of games you want to play: "))

    chance = 0
    score = 0

    game = True

    while game == True:
        
        dice_roll = random.choice(dice)
        
        print("The dice is rolled, the number is: ", dice_roll)
        
        chance += 1
        
        if chance >= N_games:
            game = False
            print("Your game quota is over")
        
        score += dice_roll
        
        print("Score is: ", score)
    





should_continue = True

players = 0

while should_continue == True:
    game()
    
    players += 1
    
    if players >= N_players:
        should_continue = False
        print("game over")
    
    play_again = input("Want to play again yes(y) or no(n): ")
    
    
    if play_again == "y":
        clear()
    elif play_again == "n":
        should_continue = False
        print("Game over")



