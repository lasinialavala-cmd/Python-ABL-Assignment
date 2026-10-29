
# University Scholarship Allocation System

MIN_AGGREGATE = 75
MIN_SUBJECT = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 300000

students = []
eligible = []
ineligible = []

n = int(input("Enter number of applicants: "))

for i in range(n):
    print(f"\nStudent {i + 1}")

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate marks (%): "))

    subject_count = int(input("Enter number of subjects: "))
    subject_marks = []

    for j in range(subject_count):
        mark = float(input(f"Enter marks for subject {j + 1} (%): "))
        subject_marks.append(mark)

    attendance = float(input("Enter attendance (%): "))
    income = float(input("Enter annual family income (Rs.): "))

    reasons = []

    if not 0 <= aggregate <= 100:
        reasons.append("Invalid aggregate marks")
    elif aggregate < MIN_AGGREGATE:
        reasons.append("Aggregate marks below 75%")

    if not subject_marks or any(
        mark < MIN_SUBJECT or mark > 100 or mark < 0
        for mark in subject_marks
    ):
        reasons.append("Subject marks do not meet requirements")

    if not 0 <= attendance <= 100:
        reasons.append("Invalid attendance percentage")
    elif attendance < MIN_ATTENDANCE:
        reasons.append("Attendance below 75%")

    if income < 0:
        reasons.append("Invalid family income")
    elif income > MAX_INCOME:
        reasons.append("Family income exceeds Rs. 300000")

    student = {
        "name": name,
        "aggregate": aggregate,
        "min_subject": min(subject_marks) if subject_marks else 0,
        "attendance": attendance,
        "income": income
    }

    if reasons:
        ineligible.append((student, reasons))
    else:
        eligible.append(student)

# Ranking rules:
# 1. Higher aggregate marks
# 2. Higher attendance
# 3. Higher minimum subject mark
# 4. Lower family income
eligible.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        -s["min_subject"],
        s["income"]
    )
)

print("\n===== UNIVERSITY SCHOLARSHIP RESULTS =====")
print("\nEligible Students (Ranked)")

if eligible:
    print(f"{'Rank':<6}{'Name':<15}{'Aggregate':<13}"
          f"{'Attendance':<13}{'Income'}")

    for rank, s in enumerate(eligible, start=1):
        print(f"{rank:<6}{s['name']:<15}"
              f"{s['aggregate']:<13.1f}"
              f"{s['attendance']:<13.1f}"
              f"Rs. {s['income']:.2f}")
else:
    print("No eligible students.")

print("\nIneligible Students")

if ineligible:
    for student, reasons in ineligible:
        print(f"\nName: {student['name']}")
        for reason in reasons:
            print(f"Reason: {reason}")
else:
    print("No ineligible students.")

print("\nScholarship allocation completed.")
