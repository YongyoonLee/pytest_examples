def calGrade(score: float)->str:
    grade: str = ""

    if score < 30.0:
        grade = "D"
    elif score < 50.0:
        grade = "C"
    elif score < 70.0:
        grade = "B"
    else:
        grade = "A"
    
    return grade

if __name__ == "__main__":
    print(calGrade(25))
    print(calGrade(30))
    print(calGrade(52))
    print(calGrade(78))