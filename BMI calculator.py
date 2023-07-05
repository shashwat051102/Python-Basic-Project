W = float(input("Enter Weight in lb: "))
H = float(input("Enter Height in inch: "))

BMI  = 703*(W/(H*H))

print("BMI is: ", BMI)

if BMI < 18.5:
    print("Underweight")
elif BMI > 18.5 and BMI < 24.9:
    print("Normal")
elif BMI > 24.9 and BMI < 29.9:
    print("Overweight")
elif BMI >= 30:
    print("Obese")