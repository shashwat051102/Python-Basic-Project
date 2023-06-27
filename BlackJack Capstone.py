############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 0
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random

import os

clear = lambda: os.system("cls")

# card numbers for games
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


#Function to compare
def compare(user_Score,computer_Score):
    if user_Score == computer_Score:
        print("Draw")
    elif user_Score > 21:
        print("you lose")
    elif computer_Score > 21:
        print("You win")
    elif computer_Score > user_Score:
        print("You lose")
    elif user_Score > computer_Score:
        print("You Win")


#Funtion to deal card
def deal_card():
    
    # Choose two random user cards
    user_cards = random.sample(cards,2)
    
    #Choose two random computer cards
    computer_cards = random.sample(cards,2)
    
    #print user cards
    print("User Cards: ",user_cards)
    
    
    #Sum of two initial user cards
    user_score = sum(user_cards)
    
    #Sum of two initial computer cards
    computer_score = sum(computer_cards)
    
    #print user score
    print("user score is: ",user_score)
    
    
    #This is to terminate while loop to increase computer score as the user or computer have already won
    win = True
    
    #This is to terminate the loop when we press n or the winner is already decided
    user = True
    
    # While loop used if user want to add another card or to decide the winner initially
    while user:
        
        # If first two cards of user is 10 and 11
        if  user_score == 21:
            
            print("You Win")
            user = False
            win = False
        
        #If first two cards of computer is 10 and 11
        elif computer_score == 21:
            print(computer_score)
            print("you lose")
            user = False
            win = False
            
        #If user want to add another card
        new_cards = input("you want to deal another card if yes type (y) and no type (n): ")
        
        #If user decided to add another card
        if new_cards == "y":
            if user_score >= 20:
                cards[0] = 1
            user_cards.append(random.choice(cards))
            print("New user deck: ", user_cards)
            user_score = sum(user_cards)
            print("User score is: ", user_score)
            
            # If user score is greater than 21
            if user_score > 21:
                user = False
                win = False
                print("You lose")
                print("Computer Score: ", computer_score)
        
        # If user decided to not to add car
        elif new_cards  == "n":
            user = False
            win = True
        
        
    
    # If the winner is not already decided 
    if win == True:
        if computer_score >= 20:
            cards[0] = 1
        # To add another card in computer cards
        while computer_score <16:
            
            computer_cards.append(random.choice(cards))
            computer_score = sum(computer_cards)
        print("New computer cards: ", computer_cards)
        print("Computer Score: ",computer_score)
        
        # Compare function to find winner
        compare(user_score,computer_score)
    
        
    

# If user want to play another game 
Should_continue = True
while Should_continue:
    deal_card()    

    Next_game = input("If you want to play again type 'y' and if you don't type 'n': ")
    if Next_game == "y":
        clear()        
        
    elif Next_game == "n":
        Should_continue = False
        print("Thanks for playing!!")


    



    
    




    