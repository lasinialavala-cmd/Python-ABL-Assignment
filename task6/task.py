
# Traffic Flow and Congestion Analysis System

roads = []
interval_totals = []

# Input validation functions
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Value must be greater than zero.")
        except ValueError:
            print("Please enter a valid integer.")


def get_nonnegative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Vehicle count cannot be negative.")
        except ValueError:
            print("Please enter a valid integer.")


# Read the number of roads and intervals
num_roads = get_positive_int("Enter number of roads: ")
num_intervals = get_positive_int("Enter number of time intervals: ")

interval_names = []

for i in range(num_intervals):
    name = input(f"Enter name of interval {i + 1}: ")
    interval_names.append(name)

# Collect road data
for i in range(num_roads):
    print(f"\nRoad {i + 1}")

    road_name = input("Enter road name: ")
    capacity = get_positive_int("Enter capacity per interval: ")

    counts = []

    for interval in interval_names:
        count = get_nonnegative_int(
            f"Enter vehicles for {interval}: "
        )
        counts.append(count)

    roads.append({
        "name": road_name,
        "capacity": capacity,
        "counts": counts
    })

# Calculate total traffic for each interval
interval_totals = [
    sum(road["counts"][i] for road in roads)
    for i in range(num_intervals)
]

# Display analysis
print("\n========== TRAFFIC ANALYSIS REPORT ==========")

over_capacity_roads = []

for road in roads:
    name = road["name"]
    capacity = road["capacity"]
    counts = road["counts"]

    total = sum(counts)
    average = total / num_intervals

    # Find peak interval
    peak_index = counts.index(max(counts))
    peak_count = counts[peak_index]
    peak_period = interval_names[peak_index]

    # Calculate congestion percentage at peak
    congestion_percentage = (peak_count / capacity) * 100

    if congestion_percentage <= 20:
        congestion = "Low"
    elif congestion_percentage <= 50:
        congestion = "Moderate"
    elif congestion_percentage <= 80:
        congestion = "High"
    else:
        congestion = "Severe"

    print(f"\nRoad: {name}")
    print(f"Total vehicles: {total}")
    print(f"Average vehicles per interval: {average:.2f}")
    print(f"Peak period: {peak_period} ({peak_count} vehicles)")
    print(f"Peak congestion percentage: {congestion_percentage:.2f}%")
    print(f"Congestion: {congestion}")

    # Identify intervals exceeding capacity
    exceeded = False

    for i, count in enumerate(counts):
        if count > capacity:
            exceeded = True
            over_capacity_roads.append(
                (name, interval_names[i], count, capacity)
            )

    print(f"Over capacity: {'Yes' if exceeded else 'No'}")

# Overall traffic analysis
print("\n========== OVERALL ANALYSIS ==========")

for i, total in enumerate(interval_totals):
    print(f"{interval_names[i]} total: {total} vehicles")

overall_peak_index = interval_totals.index(max(interval_totals))

print(f"\nOverall peak period: {interval_names[overall_peak_index]}")
print(
    f"Total vehicles during peak: "
    f"{interval_totals[overall_peak_index]}"
)

print("\nRoads exceeding capacity:")

if over_capacity_roads:
    for name, period, count, capacity in over_capacity_roads:
        print(
            f"{name} - {period} "
            f"({count} / {capacity} vehicles)"
        )
else:
    print("No roads exceeded capacity.")

print("\nTraffic analysis completed.")
