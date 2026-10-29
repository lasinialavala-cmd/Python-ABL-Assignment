
# Progressive Electricity Billing System

FIXED_CHARGE = 100
UNUSUAL_INCREASE = 30  # Percentage

def calculate_energy_charges(units):
    charges = 0

    # First 100 units
    charges += min(units, 100) * 1.50

    # Units from 101 to 200
    if units > 100:
        charges += min(units - 100, 100) * 2.50

    # Units from 201 to 500
    if units > 200:
        charges += min(units - 200, 300) * 4.00

    # Units above 500
    if units > 500:
        charges += (units - 500) * 6.00

    return charges


def calculate_bill(units):
    energy = calculate_energy_charges(units)
    fixed = FIXED_CHARGE

    surcharge = 0
    rebate = 0

    if units > 300:
        surcharge = energy * 0.05
    elif units <= 100:
        rebate = energy * 0.05

    final_bill = energy + fixed + surcharge - rebate

    return energy, fixed, surcharge, rebate, final_bill


# Input monthly consumption
while True:
    try:
        months = int(input("Enter number of months: "))
        if months > 0:
            break
        print("Number of months must be positive.")
    except ValueError:
        print("Enter a valid integer.")

consumption = []
bills = []

for i in range(months):
    while True:
        try:
            units = float(
                input(f"Enter Month {i + 1} consumption (units): ")
            )
            if units >= 0:
                break
            print("Consumption cannot be negative.")
        except ValueError:
            print("Enter a valid numeric value.")

    consumption.append(units)
    bills.append(calculate_bill(units))

# Display bills
print("\n===== ELECTRICITY BILLING REPORT =====")

unusual_count = 0

for i in range(months):
    energy, fixed, surcharge, rebate, final_bill = bills[i]

    print(f"\nMonth {i + 1}")
    print(f"Consumption: {consumption[i]:.2f} units")
    print(f"Energy Charges: Rs. {energy:.2f}")
    print(f"Fixed Charges: Rs. {fixed:.2f}")
    print(f"Surcharge: Rs. {surcharge:.2f}")
    print(f"Rebate: Rs. {rebate:.2f}")
    print(f"Final Bill: Rs. {final_bill:.2f}")

    if i > 0:
        previous_bill = bills[i - 1][4]

        if previous_bill > 0:
            change = (
                (final_bill - previous_bill) / previous_bill
            ) * 100

            print(f"Change from previous bill: {change:.2f}%")

            if change > UNUSUAL_INCREASE:
                print("WARNING: Unusual increase detected!")
                unusual_count += 1
            elif change < 0:
                print("Bill decreased compared with previous month.")
            else:
                print("No unusual increase detected.")
        elif final_bill > 0:
            print("Bill increased from zero.")
            print("Percentage change is undefined.")

# Summary
total = sum(bill[4] for bill in bills)
average = total / months

print("\n===== SUMMARY =====")
print(f"Total Bills: Rs. {total:.2f}")
print(f"Average Monthly Bill: Rs. {average:.2f}")
print(f"Unusual Increases: {unusual_count}")
