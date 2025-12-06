#https://www.hackerrank.com/challenges/grading/problem
#Feladatleírást elcseszték, 33 alatt van írva 35 alatt helyett.

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] <= 35:
            continue
        osztva = grades[i] // 5 + 1
        if osztva*5 - grades[i] < 3:
            grades[i] = osztva*5
    return grades


