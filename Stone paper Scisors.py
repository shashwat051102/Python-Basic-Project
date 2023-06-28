import random
list = ["s", "p" , "sc"]
S_P_Sc = random.choice(list)
# print(S_P_Sc)
M = input("Stone Paper Scissors? :  ")
U_score = 0
C_score = 0
print("Computer guess: ", S_P_Sc)
while M !="end":

    if M == S_P_Sc:
        print("Draw")
        M = input("Stone Paper Scissors? :  ")
        S_P_Sc = random.choice(list)

        print("Computer guess: ", S_P_Sc)
        U_score += 1
        C_score += 1
    elif M == "p" and S_P_Sc == "s":
        print("You win")
        M = input("Stone Paper Scissors? :  ")

        S_P_Sc = random.choice(list)
        print("Computer guess: ", S_P_Sc)
        U_score += 1
    elif M == "sc" and S_P_Sc == "p":
        print("You win")
        M = input("Stone Paper Scissors? :  ")

        S_P_Sc = random.choice(list)
        print("Computer guess: ", S_P_Sc)
        U_score += 1
    elif M == "s" and S_P_Sc == "sSc":
        print("You win")
        M = input("Stone Paper Scissors? :  ")

        S_P_Sc = random.choice(list)
        print("Computer guess: ", S_P_Sc)
        U_score += 1
    else:
        print("You lose")
        M = input("Stone Paper Scissors? :  ")

        S_P_Sc = random.choice(list)

        print("Computer guess: ", S_P_Sc)
        C_score += 1
print("User Score: ", U_score)
print("Computer score: ", C_score)
if U_score > C_score:
    print("User wins")
elif C_score == U_score:
    print("Draw")
else:
    print("Computer Wins")