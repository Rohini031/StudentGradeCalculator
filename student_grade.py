def valid_mark(mark):
    return 0 <= mark <= 100


def average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)


def grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def is_pass(marks):
    return all(mark >= 40 for mark in marks)


if __name__ == "__main__":
    name = input("Enter student name: ")
    department = input("Enter department: ")
    semester = input("Enter semester: ")

    marks = []
    n = int(input("Enter number of subjects: "))

    for i in range(n):
        mark = float(input(f"Enter mark for subject {i + 1}: "))
        if valid_mark(mark):
            marks.append(mark)
        else:
            print("Invalid marks! Enter marks between 0 and 100.")
            break

    avg = average(marks)
    student_grade = grade(avg)

    print("\n------- STUDENT RESULT -------")
    print("Name:", name)
    print("Department:", department)
    print("Semester:", semester)
    print("Average:", avg)
    print("Grade:", student_grade)
    print("Status:", "Pass" if is_pass(marks) else "Fail")