
# Student Performance Trend Analysis

students = []

# Input validation helper
def get_integer(prompt, minimum=1):
    while True:
        try:
            value = int(input(prompt))
            if value >= minimum:
                return value
            print(f"Enter a value greater than or equal to {minimum}.")
        except ValueError:
            print("Invalid input. Enter an integer.")


def get_marks(prompt):
    while True:
        try:
            marks = float(input(prompt))
            if 0 <= marks <= 100:
                return marks
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a numeric mark.")


# Input dimensions
n = get_integer("Enter number of students: ")
subject_count = get_integer("Enter number of subjects: ")
exam_count = get_integer("Enter number of examinations: ")

for i in range(n):
    print(f"\nStudent {i + 1}")
    name = input("Enter student name: ")

    subjects = {}

    for j in range(subject_count):
        subject = input(f"Enter subject {j + 1} name: ")
        exam_marks = []

        for k in range(exam_count):
            mark = get_marks(
                f"Enter {subject} marks for Exam {k + 1}: "
            )
            exam_marks.append(mark)

        subjects[subject] = exam_marks

    students.append({"name": name, "subjects": subjects})


# Analyze and display results
for student in students:
    name = student["name"]
    subjects = student["subjects"]

    print("\n" + "=" * 45)
    print("STUDENT PERFORMANCE REPORT")
    print("=" * 45)
    print("Student Name:", name)

    # Calculate examination averages
    exam_averages = []

    for exam in range(exam_count):
        total = sum(
            marks[exam] for marks in subjects.values()
        )
        average = total / subject_count
        exam_averages.append(average)

    print("\nEXAMINATION-WISE AVERAGES")

    for i, average in enumerate(exam_averages):
        print(f"Exam {i + 1} Average: {average:.2f}")

    # Compare consecutive examination averages
    print("\nOVERALL PERFORMANCE TRENDS")

    for i in range(1, exam_count):
        change = exam_averages[i] - exam_averages[i - 1]

        if change > 0:
            print(
                f"Exam {i} to Exam {i + 1}: "
                f"Improved by {change:.2f} marks"
            )
        elif change < 0:
            print(
                f"Exam {i} to Exam {i + 1}: "
                f"Declined by {abs(change):.2f} marks"
            )
        else:
            print(
                f"Exam {i} to Exam {i + 1}: "
                "No change"
            )

    # Subject-wise trends
    print("\nSUBJECT-WISE ANALYSIS")
    weak_subjects = []

    for subject, marks in subjects.items():
        print(f"{subject}: {', '.join(map(str, marks))}")

        if all(mark < 40 for mark in marks):
            weak_subjects.append(subject)

        change = marks[-1] - marks[0]

        if change > 0:
            print(f"Trend: Improved by {change:.2f} marks")
        elif change < 0:
            print(f"Trend: Declined by {abs(change):.2f} marks")
        else:
            print("Trend: No overall change")

    # Identify consistently weak subjects
    print("\nCONSISTENTLY WEAK SUBJECTS")

    if weak_subjects:
        for subject in weak_subjects:
            print(subject)
    else:
        print("No consistently weak subjects.")

    # Overall average across all exams and subjects
    all_marks = [
        mark
        for marks in subjects.values()
        for mark in marks
    ]

    overall_average = sum(all_marks) / len(all_marks)

    # Student classification
    if overall_average >= 85:
        classification = "Excellent"
    elif overall_average >= 70:
        classification = "Good"
    elif overall_average >= 50:
        classification = "Average"
    else:
        classification = "Needs Improvement"

    print(f"\nOVERALL AVERAGE: {overall_average:.2f}")
    print("STUDENT CLASSIFICATION:", classification)
    print("=" * 45)
