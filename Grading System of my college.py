import numpy as np
import math

#Question 1

def average(lst):
  
    return  sum(lst)/len(lst)



Exam_Scores = [72,81,44,68,90,53,80,75,74,65,50,92,85,69,41,73,70,86,61,65,79,94,69]

Avg_Exam_score = average(Exam_Scores)
print("Average exam score: ", round(Avg_Exam_score,2))


S_d = np.std(Exam_Scores)

print("Standard deviation of Exam score is: ", round(S_d,2))

for i in range(0,len(Exam_Scores)):
    if Exam_Scores[i]>= Avg_Exam_score + 1.3*(S_d):
        print("Grades: A")
    elif Avg_Exam_score + 0.5*(S_d) <= Exam_Scores[i] and Exam_Scores[i] < Avg_Exam_score + 1.3*S_d:
        print("Grade: B")
    elif Avg_Exam_score - 0.5*S_d <= Exam_Scores[i] and Exam_Scores[i] < Avg_Exam_score + 0.5*S_d:
        print("Grade: C")
    elif Avg_Exam_score - 1.3*S_d <= Exam_Scores[i] and Exam_Scores[i] < Avg_Exam_score - 0.5*S_d:
        print("Grade: D")
    elif Exam_Scores[i] < Avg_Exam_score - 1.3*S_d:
        print("Grade: F")