x = 0
y = 0

N_steps = int(input("Enter the Number of steps: "))

for i in range(0,N_steps):
    Direction = input("Enter the direction UP,DOWN,LEFT,RIGHT: ")
    steps = int(input(f"Enter the number of steps in {Direction} Direction: "))
    Direction = Direction.lower()
    
    if Direction == "up":
        y += steps
    elif Direction == "down":
        y -= steps
    elif Direction == "right":
        x += steps
    elif Direction == "left":
        x -= steps
    

# total_steps = int(up) + int(down) + int(left) + int(right)
# if total_steps == N_steps:
        
        
distance = pow(x,2) + pow(y,2)
Distance = pow(distance,0.5)
print(f"The distsnce from (0,0) is ({x},{y}) is: ", round(Distance))
