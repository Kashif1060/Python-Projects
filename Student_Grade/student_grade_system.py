print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

math = float(input("Enter Math marks: "))
english = float(input("Enter English marks: "))
science = float(input("Enter Science marks: "))
computer = float(input("Enter Computer marks: "))
urdu = float(input("Enter Urdu marks: "))

total = math + english + science + computer + urdu
percentage = (total / 500) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== RESULT =====")
print("Student:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)

if grade == "F":
    print("Status: Fail")
else:
    print("Status: Pass")
