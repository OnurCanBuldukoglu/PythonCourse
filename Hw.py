student = ["Onur Can", "Buldukoğlu"]
check = False

for i in range(3):
    name = input("Please enter your name: ").title()
    surname = input("Please enter your surname: ").title()
    if name == student[0] and surname == student[1]:
        check = True
        print("Welcome {} {}".format(student[0], student[1]))
        break
if not check:
    print("Please try again later.")
    exit()

course_input = input("Please enter the names of your courses: ").title()
courses = course_input.split()

def num_check(mylist):
    if len(mylist) < 3:
        return "You failed in class. You cannot take fewer than 3 courses."
    elif len(mylist) > 5:
        return "You cannot take more than 5 courses."
    else:
        return "Thank you."

print(num_check(courses))

course_notes = {"midterm": 23, "final": 12, "project": 31}  #notlar kullanıcıdan alınmadı. Deneme için elle değiştirilebilir.
grade = (course_notes["midterm"]*0.3 + course_notes["final"]*0.5 + course_notes["project"]*0.2)

if grade >= 90:
    grade_letter = "AA"
elif 70 <= grade < 90:
    grade_letter = "BB"
elif 50 <= grade < 70:
    grade_letter = "CC"
elif 30 <= grade < 50:
    grade_letter = "DD"
elif grade < 30:
    grade_letter = "FF"

if 3 <= len(courses) <= 5:
    while True:
        chosen_course = input("Please choose a course to take exam: ").title()
        if chosen_course in courses:
            break
        else:
            print("You are not registered for that course.")
    if grade_letter == "FF":
        print("You failed the class with {}, with the grade of {:.2f}. ".format(grade_letter, grade))
    else:
        print("You passed the class with {}, with the passing grade of {:.2f}.".format(grade_letter, grade))
