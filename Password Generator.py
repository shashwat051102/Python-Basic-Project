#Password generator project

import random

Alphabates = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Numbers = ["0","1","2","3","4","5","6","7","8","9"]
Symbols = ["!", "#", "$","%","&","(",")","*","+"]

print("Welcome to the py password generator!!")

nr_letters = int(input("How many letters would you want in your password?\n"))
nr_Numbers = int(input("How many numbers would you want in your password?\n"))
nr_Symbols = int(input("How many symbols would you like in your password?\n"))

#Easy Level
# password = ""
# for char in range(0,nr_letters + 1):
    
#     password += random.choice(Alphabates)
    


# for char in range(0,nr_Numbers + 1):
    
#     password += random.choice(Numbers)



# for char in range(0,nr_Symbols + 1):
    
#     password += random.choice(Symbols)

# print(password)


#Hard level


password_list = []
for char in range(0,nr_letters + 1):
    
    password_list += random.choice(Alphabates)
    # password_list.append(random.choice(Alphabates))
    


for char in range(0,nr_Numbers + 1):
    
    password_list += random.choice(Numbers)



for char in range(0,nr_Symbols + 1):
    
    password_list += random.choice(Symbols)

# print(password_list)

random.shuffle(password_list)

print("Your password is: ", password_list)


password = ""

for char in password_list:
    password += char
    
print("Here is your password: ", password)