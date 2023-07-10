import random

import os

clear = lambda: os.system("cls")

power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


def game():
    catch = input("Want to catch a new pokemon?: ")
    your_pokemon = []
    if catch == "y":
        pokemon_power = random.choice(power)
        print("Power of new pokemon is: ", pokemon_power)
        your_pokemon.append(pokemon_power)
        your_pokemon.sort()
    elif catch == "n":
        print("No problem")
        
    max_power = your_pokemon[0]
    print("Max power: ", max_power)
    min_power = your_pokemon[-1]
    print("Min power: ", min_power)


should_continue = True


while should_continue == True:
    game()
    play_again = input("Want to play again(y or n): ")
    if play_again == "y":
        
    
    elif play_again == "n":
        print("Thanks for playing")
        should_continue = False
