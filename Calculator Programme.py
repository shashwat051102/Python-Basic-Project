# calculator

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""





# Adding
def add(n1,n2):
    return n1 + n2

# Subtraction

def sub(n1, n2):
    return n1 - n2

# Multiplication

def mult(n1, n2):
    return n1 * n2

# Division

def div(n1, n2):
    return n1 / n2


operations = {
    "+" : add,
    "-" : sub,
    "*" : mult,
    "/": div,
}


#Recursion



def calculator():
    print(logo)
    
    num1 = float(input("What is the first number?: "))


    for symbol in operations:
        print(symbol)


    Should_continue = True


    while Should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        if operation_symbol == "+":
            answer = num1 + num2
            
        elif operation_symbol == "-":
            answer = num1 - num2 
        elif operation_symbol == "*":
            answer = num1 * num2
        elif operation_symbol == "/":
            answer = num1 / num2

        answer = round(answer,2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            Should_continue = False
            calculator()
calculator()
    # operation_symbol = input("Pick another operation symbol from the line above: ")
    # num3 = int(input("Whats the next number?: "))
    # calculation_function = operations[operation_symbol]
    # second_answer = calculation_function(first_answer,num3)

    # print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

# Print vs return

