# Student Grade System

name = input("Enter student name: ")
marks = int(input("Enter marks: "))

# Grade logic
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"

if grade == "A":
    print("Excellent performance")
elif grade == "B":
    print("Good job")
elif grade == "C":
    print("Needs improvement")
else:
    print("Work harder")

# Final output
print("\nStudent Name:", name)
print("Marks:", marks)
print("Grade:", grade)