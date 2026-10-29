
# Manufacturing Quality Control Matrix

THRESHOLD = 5.0

batches = []

n = int(input("Enter the number of batches: "))

if n <= 0:
    print("Number of batches must be positive.")
else:
    for i in range(n):
        print(f"\nBatch {i + 1}")

        product = input("Enter product name: ")
        batch_no = input("Enter batch number: ")

        while True:
            try:
                production = int(input("Enter production quantity: "))
                defective = int(input("Enter defective units: "))

                if production <= 0:
                    print("Production quantity must be positive.")
                elif defective < 0 or defective > production:
                    print("Defective units must be between 0 and production quantity.")
                else:
                    break
            except ValueError:
                print("Please enter valid whole numbers.")

        defect_percentage = (defective / production) * 100

        if defect_percentage > THRESHOLD:
            status = "Needs Inspection"
        else:
            status = "Acceptable"

        batches.append({
            "product": product,
            "batch": batch_no,
            "production": production,
            "defective": defective,
            "percentage": defect_percentage,
            "status": status
        })

    print("\n========== QUALITY CONTROL MATRIX ==========")
    print(f"{'Product':<12}{'Batch':<10}{'Produced':>10}"
          f"{'Defects':>10}{'Defect %':>12}  Status")
    print("-" * 75)

    for b in batches:
        print(f"{b['product']:<12}{b['batch']:<10}"
              f"{b['production']:>10}{b['defective']:>10}"
              f"{b['percentage']:>11.2f}%  {b['status']}")

    print("\nBatches Exceeding the 5% Defect Threshold:")
    flagged = [b for b in batches if b["percentage"] > THRESHOLD]

    if flagged:
        for b in flagged:
            print(f"{b['product']} - Batch {b['batch']}: "
                  f"{b['percentage']:.2f}% defects")
    else:
        print("No batches exceed the threshold.")

    total_produced = sum(b["production"] for b in batches)
    total_defective = sum(b["defective"] for b in batches)
    overall_percentage = total_defective / total_produced * 100

    print(f"\nTotal units produced: {total_produced}")
    print(f"Total defective units: {total_defective}")
    print(f"Overall defect percentage: {overall_percentage:.2f}%")
