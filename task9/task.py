
# Campus Resource Allocation Under Constraints

resources = ["Projectors", "Laptops", "Microphones"]

available = {}

print("Enter the available campus resources:")
for resource in resources:
    while True:
        try:
            quantity = int(input(f"{resource}: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
            else:
                available[resource] = quantity
                break
        except ValueError:
            print("Enter a valid whole number.")

n = int(input("\nEnter the number of activities: "))

activities = []

for i in range(n):
    print(f"\nActivity {i + 1}")
    name = input("Activity name: ")

    while True:
        try:
            priority = int(input("Priority (1 = highest): "))
            if priority <= 0:
                print("Priority must be a positive number.")
            else:
                break
        except ValueError:
            print("Enter a valid whole number.")

    requirements = {}
    for resource in resources:
        while True:
            try:
                quantity = int(input(f"{resource} required: "))
                if quantity < 0:
                    print("Requirement cannot be negative.")
                else:
                    requirements[resource] = quantity
                    break
            except ValueError:
                print("Enter a valid whole number.")

    activities.append({
        "name": name,
        "priority": priority,
        "requirements": requirements
    })

# Sort by priority; preserve input order for equal priorities.
activities.sort(key=lambda a: a["priority"])

allocations = []

for activity in activities:
    for resource in resources:
        required = activity["requirements"][resource]
        remaining = available[resource]

        if required <= remaining:
            allocated = required
            shortage = 0
        else:
            allocated = 0
            shortage = required - remaining

        available[resource] -= allocated

        allocations.append({
            "activity": activity["name"],
            "priority": activity["priority"],
            "resource": resource,
            "required": required,
            "allocated": allocated,
            "shortage": shortage
        })

print("\n========== RESOURCE ALLOCATION MATRIX ==========")
print(f"{'Activity':<15}{'Priority':>9}{'Resource':<15}"
      f"{'Required':>10}{'Allocated':>11}{'Shortage':>10}")
print("-" * 70)

for item in allocations:
    print(f"{item['activity']:<15}{item['priority']:>9}"
          f"{item['resource']:<15}{item['required']:>10}"
          f"{item['allocated']:>11}{item['shortage']:>10}")

print("\n========== REMAINING RESOURCES ==========")
for resource in resources:
    print(f"{resource}: {available[resource]}")

print("\n========== ACTIVITIES WITH SHORTAGES ==========")
shortage_activities = set()

for item in allocations:
    if item["shortage"] > 0:
        shortage_activities.add(item["activity"])
        print(f"{item['activity']} - {item['resource']}: "
              f"short by {item['shortage']}")

if not shortage_activities:
    print("All resource requirements were satisfied.")
