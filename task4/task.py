
# Employee Payroll and Deduction Analysis

def calculate_tax(gross):
    tax = 0

    # First Rs. 20,000 - 0%
    if gross > 20000:
        tax += min(gross - 20000, 30000) * 0.05

    # Rs. 50,001 to Rs. 100,000 - 10%
    if gross > 50000:
        tax += min(gross - 50000, 50000) * 0.10

    # Above Rs. 100,000 - 20%
    if gross > 100000:
        tax += (gross - 100000) * 0.20

    return tax


employees = []

while True:
    try:
        n = int(input("Enter number of employees: "))
        if n > 0:
            break
        print("Number of employees must be positive.")
    except ValueError:
        print("Enter a valid integer.")


for i in range(n):
    print(f"\nEmployee {i + 1}")

    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")

    while True:
        try:
            basic = float(input("Enter basic salary: "))
            overtime_hours = float(input("Enter overtime hours: "))
            hourly_rate = float(input("Enter hourly rate: "))
            incentive = float(input("Enter incentive: "))

            if basic > 0 and overtime_hours >= 0 and \
               hourly_rate >= 0 and incentive >= 0:
                break

            print("Invalid salary or overtime details.")
        except ValueError:
            print("Enter valid numeric values.")

    # Allowances
    hra = basic * 0.20
    da = basic * 0.10

    # Overtime pay
    overtime_pay = overtime_hours * hourly_rate * 1.5

    # Gross salary
    gross = basic + hra + da + overtime_pay + incentive

    # Deductions
    pf = basic * 0.12
    tax = calculate_tax(gross)

    total_deductions = pf + tax

    # Net salary
    net = gross - total_deductions

    employee = {
        "id": emp_id,
        "name": name,
        "basic": basic,
        "hra": hra,
        "da": da,
        "overtime": overtime_pay,
        "incentive": incentive,
        "gross": gross,
        "pf": pf,
        "tax": tax,
        "deductions": total_deductions,
        "net": net
    }

    employees.append(employee)


# Display salary statements
print("\n========== PAYROLL STATEMENTS ==========")

for emp in employees:
    print("\n--------------------------------------")
    print("EMPLOYEE SALARY STATEMENT")
    print("--------------------------------------")

    print(f"Employee ID: {emp['id']}")
    print(f"Employee Name: {emp['name']}")

    print(f"Basic Salary: Rs. {emp['basic']:.2f}")
    print(f"HRA: Rs. {emp['hra']:.2f}")
    print(f"DA: Rs. {emp['da']:.2f}")
    print(f"Overtime Pay: Rs. {emp['overtime']:.2f}")
    print(f"Incentive: Rs. {emp['incentive']:.2f}")

    print(f"Gross Salary: Rs. {emp['gross']:.2f}")
    print(f"PF Deduction: Rs. {emp['pf']:.2f}")
    print(f"Progressive Tax: Rs. {emp['tax']:.2f}")
    print(f"Total Deductions: Rs. {emp['deductions']:.2f}")

    print(f"Net Salary: Rs. {emp['net']:.2f}")


# Payroll summary
total_gross = sum(emp["gross"] for emp in employees)
total_deductions = sum(emp["deductions"] for emp in employees)
total_net = sum(emp["net"] for emp in employees)

print("\n========== PAYROLL SUMMARY ==========")

print(f"Total Employees: {len(employees)}")
print(f"Total Gross Salary: Rs. {total_gross:.2f}")
print(f"Total Deductions: Rs. {total_deductions:.2f}")
print(f"Total Net Salary: Rs. {total_net:.2f}")

print("\nPayroll calculation completed.")
