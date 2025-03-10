grade = int(input("Type your score: "))
if grade < 0 or grade > 100:
    print("Invalid score! Please enter a value between 0 and 100")
elif grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 0:
    print("Grade: D")
else:
    print("Grade: F")