# Input student details
name = input("Enter student name: ")
sub1 = int(input("Enter marks for Subject 1: "))
sub2 = int(input("Enter marks for Subject 2: "))
sub3 = int(input("Enter marks for Subject 3: "))

# Calculate total, average, and percentage
total = sub1 + sub2 + sub3
average = total / 3
percentage = (total / 300) * 100

# Assign grade
if average >= 80:
    grade = 'A'
elif average >= 70:
    grade = 'B'
elif average >= 50:
    grade = 'C'
else:
    grade = 'F'


is_pass = sub1 >= 40 and sub2 >= 40 and sub3 >= 40  # Check pass (all subjects ≥ 40)


scholarship = average >= 85 and sub1 >= 80 and sub2 >= 80 and sub3 >= 80  # Check scholarship eligibility (avg ≥ 85 and all marks ≥ 80)


sub1 += 10  # Add to bonus
sub2 += 10
sub3 += 10


total = sub1 + sub2 + sub3  #calculate after bonus
average = total / 3

# Output results
print(" Student Result Report ")
print(f"Name: {name}")
print(f"Total Marks: {total}")
print(f"Average: {average:.2f}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print("Pass Status:", "Passed" if is_pass else "Failed")
print("Scholarship Eligible:", "Yes" if scholarship else "No")
print(f"Marks after Bonus: {sub1}, {sub2}, {sub3}")
print(f"New Total: {total}")
print(f"New Average: {average:.2f}")