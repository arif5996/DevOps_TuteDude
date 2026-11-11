
def check_grade(score: int):
    if score>=90:
        return "A"
    elif (score >= 80) and (score <= 89):
        return "B"
    elif (score >= 70) and (score <= 79):
        return "C"
    elif (score >= 60) and (score <= 69):
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    score = int(input("Enter the student Scope: "))
    print(f"Student's Grade is: {check_grade(score)}")

