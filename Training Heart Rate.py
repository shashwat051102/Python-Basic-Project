import numpy as np
import math



Gender = input("Male or Female: ")
if Gender == "Male":
    age_M = int(input("Enter the age of male: "))
    RHR = int(input("Enter the Resting Heart Rate: "))
    F_L_C = input("Enter fitness level (High, Medium, Low): ")
    if F_L_C == "High":
        INTEN = 0.8
    elif F_L_C == "Medium":
        INTEN = 0.65
    elif F_L_C == "Low":
        INTEN = 0.55 
    
    E = 0.033*(age_M-104.3)
    M_E = 1+math.exp(E)
    MHR = 203.7/M_E
    print("MHR is: ", round(MHR,2))
    
    THR = (MHR-RHR)*INTEN+RHR
    print("Male Training Heart Rate is: ",round(THR,2))
    
    
elif Gender == "Female":
    age_F = int(input("Enter the age of Female: "))
    RHR = int(input("Enter the Resting Heart Rate: "))
    F_L_C = input("Enter fitness level (High, Medium, Low): ")
    if F_L_C == "High":
        INTEN = 0.8
    elif F_L_C == "Medium":
        INTEN = 0.65
    elif F_L_C == "Low":
        INTEN = 0.55 
    
    E = 0.0453*(age_F-107.3)
    F_E = 1+math.exp(E)
    MHR = 203.7/F_E
    print("MHR is: ", round(MHR,2))
    
    THR = (MHR-RHR)*INTEN+RHR
    print("Female Training Heart Rate is: ",round(THR,2))

