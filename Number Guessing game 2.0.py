# Import random module
import random



# Function to play this game 
def choice():
    # Upper value of range to choose for computer
    x = int(input("Enter the Upper value: "))
    
    # for choosing random value 
    C_Choice = random.randint(1,x)
    
    # To determine the level of the game so that we can determine the chances a player can play
    Level = input("Enter the level(Easy, Medium and Hard): ").lower()
    
    # to initialise the counting for number of chances played
    count = 0
    
    # these are to determine the number of chances at a given level 
    if Level == "easy":
        Max_choice = 15
    elif Level == "medium":
        Max_choice = 10
    elif Level == "hard":
        Max_choice = 5
    
    
    # this gives the condition to while loop
    game = True
    
    # while loop to play the game until player won the game or number of chances completed
    while game == True:
        
        # to take note of number of chances
        count += 1
        
        # to give condition to loop if number of chances is completed
        if count >= Max_choice:
            print("No more chances left")
            game = False
        
        # This is for user to choose the number
        User_choice = int(input("Enter your choice: "))
        
        
        if User_choice < C_Choice:
            print("Too low")
        elif User_choice > C_Choice:
            print("Too High")
        else:
            print("Congrats you are right!!!!")
            game = False
            

print(choice())

