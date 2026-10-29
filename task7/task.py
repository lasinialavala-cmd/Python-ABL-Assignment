
# Hackathon Team Formation and Ranking System

MIN_SIZE = 2
MAX_SIZE = 4
ROUNDS = ["Coding", "Innovation", "Presentation"]

teams = []


def get_integer(prompt, minimum, maximum=None):
    while True:
        try:
            value = int(input(prompt))
            if value >= minimum and (
                maximum is None or value <= maximum
            ):
                return value
            print("Invalid value. Please try again.")
        except ValueError:
            print("Please enter a valid integer.")


def get_score(prompt):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid numeric score.")


# Input number of teams
num_teams = get_integer("Enter number of teams: ", 1)

for i in range(num_teams):
    print(f"\n--- Team {i + 1} ---")

    team_name = input("Enter team name: ").strip()

    while not team_name:
        print("Team name cannot be empty.")
        team_name = input("Enter team name: ").strip()

    # Validate team size
    member_count = get_integer(
        f"Enter number of members ({MIN_SIZE}-{MAX_SIZE}): ",
        MIN_SIZE,
        MAX_SIZE
    )

    members = []
    round_totals = {round_name: 0 for round_name in ROUNDS}

    for j in range(member_count):
        print(f"\nMember {j + 1}")
        student_name = input("Enter student name: ").strip()

        while not student_name:
            print("Student name cannot be empty.")
            student_name = input("Enter student name: ").strip()

        scores = {}

        for round_name in ROUNDS:
            score = get_score(
                f"Enter {round_name} score (0-100): "
            )
            scores[round_name] = score
            round_totals[round_name] += score

        members.append({
            "name": student_name,
            "scores": scores
        })

    total_score = sum(round_totals.values())

    teams.append({
        "name": team_name,
        "members": members,
        "round_totals": round_totals,
        "total": total_score
    })


# Ranking rules:
# 1. Higher total score
# 2. Higher Presentation score
# 3. Higher Coding score
# 4. Alphabetical team name
teams.sort(
    key=lambda team: (
        -team["total"],
        -team["round_totals"]["Presentation"],
        -team["round_totals"]["Coding"],
        team["name"].casefold()
    )
)


# Display final ranking
print("\n========== HACKATHON TEAM RANKING ==========")

for rank, team in enumerate(teams, start=1):
    print(f"\nRank: {rank}")
    print(f"Team: {team['name']}")

    member_names = [
        member["name"] for member in team["members"]
    ]
    print("Members:", ", ".join(member_names))

    for round_name in ROUNDS:
        print(
            f"{round_name} Score: "
            f"{team['round_totals'][round_name]:.2f}"
        )

    print(f"Total Score: {team['total']:.2f}")

print("\n========== FINAL RESULTS ==========")

for rank, team in enumerate(teams, start=1):
    print(
        f"Rank {rank}: {team['name']} "
        f"- Total Score: {team['total']:.2f}"
    )

print("\nHackathon ranking completed.")
