# Takes student's name as input
student_name = input("Enter student name: ")

# Takes marks for 3 subjects
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

# Calculates Total and Average marks
total_marks = mark1 + mark2 + mark3
average_marks = total_marks / 3

# Determines the grade
if average_marks >= 80:
    grade = "A+"
elif average_marks >= 70:
    grade = "A"
elif average_marks >= 60:
    grade = "B"
elif average_marks >= 50:
    grade = "C"
else:
    grade = "F"

# Displays the result using a formatted string (f-string)
print("\n* Student Result *")
print(f"\nStudent Name: {student_name}")
print(f"Total Marks: {total_marks:.0f}")
print(f"Average: {average_marks:.2f}")
print(f"Grade: {grade}")