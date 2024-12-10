while True:
    try:
        student_1 = str(input("Enter first student name: "))
        student_2 = str(input("Enter second student name: "))
        student_3 = str(input("Enter third student name: "))

        grade_1 = int(input("Enter first student grade(1-6): "))
        grade_2 = int(input("Enter second student grade(1-6): "))
        grade_3 = int(input("Enter third student grade(1-6): "))

        if not all(grade in range(1, 7) for grade in (grade_1, grade_2, grade_3)):
            print("Grades must be between 1 and 6, try again!")
            continue

        students = {
            student_1: grade_1, 
            student_2: grade_2,
            student_3: grade_3
        }

        question_1 = str(input("You wanna add other student? (yes/no)"))
        if question_1.lower() == "yes":
            new_student = str(input("Enter new student name: "))
            new_grade = int(input("Enter new student grade: "))
            students[new_student] = new_grade

            if new_grade in range(1,7):
                students[new_student] = new_grade
            else:
                print("Grade must be between 1 and 6. Try again.")
                continue
        elif question_1.lower() == "no":
            print("Sure!")
            continue
        else:
            print("Invalid value")
            continue

        print("Let's check students grades!")
        for name, grade in students.items():
            print(f"Student: {name}, Grade: {grade}")
        
    except ValueError:
        print("Invalid value")
        continue
    break