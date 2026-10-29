
# Multi-Stage Scholarship Shortlisting

MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 300000

quota = int(input("Enter scholarship quota: "))
n = int(input("Enter number of applicants: "))

students = []
rejected = []

if quota < 0 or n < 0:
    print("Quota and number of applicants cannot be negative.")
else:
    for i in range(n):
        print(f"\nApplicant {i + 1}")

        name = input("Student name: ")

        marks = []
        for j in range(3):
            while True:
                mark = float(input(f"Enter mark for subject {j + 1} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                print("Marks must be between 0 and 100.")

        while True:
            attendance = float(input("Attendance percentage: "))
            if 0 <= attendance <= 100:
                break
            print("Attendance must be between 0 and 100.")

        income = float(input("Annual family income (Rs.): "))

        aggregate = sum(marks) / len(marks)
        minimum_mark = min(marks)

        reasons = []

        if aggregate < MIN_AGGREGATE:
            reasons.append("Aggregate below 75%")
        if minimum_mark < MIN_SUBJECT_MARK:
            reasons.append("A subject mark below 60%")
        if attendance < MIN_ATTENDANCE:
            reasons.append("Attendance below 75%")
        if income > MAX_INCOME:
            reasons.append("Family income exceeds Rs. 3,00,000")

        student = {
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "minimum_mark": minimum_mark,
            "income": income
        }

        if not reasons:
            students.append(student)
        else:
            rejected.append((name, reasons))

    # Ranking: aggregate descending, attendance descending,
    # minimum subject mark descending, income ascending.
    students.sort(
        key=lambda s: (
            -s["aggregate"],
            -s["attendance"],
            -s["minimum_mark"],
            s["income"]
        )
    )

    shortlisted = students[:quota]

    print("\n========== SCHOLARSHIP SHORTLIST ==========")
    if shortlisted:
        print(f"{'Rank':<6}{'Name':<18}{'Aggregate':>12}"
              f"{'Attendance':>13}{'Income':>14}")
        print("-" * 63)

        for rank, s in enumerate(shortlisted, start=1):
            print(f"{rank:<6}{s['name']:<18}"
                  f"{s['aggregate']:>11.2f}%"
                  f"{s['attendance']:>12.2f}%"
                  f"{s['income']:>14.2f}")
    else:
        print("No students shortlisted.")

    print(f"\nScholarships awarded: {len(shortlisted)} out of {quota}")

    if len(students) > quota:
        print("\nEligible students not selected due to quota:")
        for s in students[quota:]:
            print(s["name"])

    print("\n========== REJECTED APPLICANTS ==========")
    if rejected:
        for name, reasons in rejected:
            print(f"{name}: {', '.join(reasons)}")
    else:
        print("No applicants rejected on eligibility criteria.")
