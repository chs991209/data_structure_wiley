print("Welcome to the GPA calculator.")
print("Please enter all your letter grades, one per line.")
print("Enter a blank line to designate the end.")

points = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.67,
    "B+": 3.33,
    "B": 3.0,
    "B-": 2.67,
    "C+": 2.33,
    "C": 2.0,
    "C-": 1.67,
    "D+": 1.33,
    "D": 1.0,
    "F": 0.0,
}

total_points = 0
num_courses = 0

while True:
    grade = input("Enter grade (or press Enter to finish): ").strip().upper()
    if not grade:  # empty line was entered
        break
    elif grade in points:
        num_courses += 1
        total_points += points[grade]
    else:
        print("Unknown grade '{0}' being ignored".format(grade))

if num_courses > 0:
    gpa = total_points / num_courses
    print("Your GPA is {:.3f}".format(gpa))
else:
    print("No grades were entered.")
