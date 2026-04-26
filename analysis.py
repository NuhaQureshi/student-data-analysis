# Student Data Analysis

students = [
    {"name": "Rahul", "marks": 85},
    {"name": "Anita", "marks": 78},
    {"name": "Kiran", "marks": 92},
    {"name": "Sneha", "marks": 88}
]

# Calculate average marks
total = 0
for student in students:
    total += student["marks"]

average = total / len(students)

# ✅ ADD YOUR CODE HERE
if average > 90:
    print("Excellent performance")
elif average > 75:
    print("Good performance")
else:
    print("Needs improvement")

# Find topper
topper = max(students, key=lambda x: x["marks"])

print("Average Marks:", average)
print("Topper:", topper["name"], "-", topper["marks"])