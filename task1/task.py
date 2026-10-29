
# ATM Menu-Driven Banking Simulation

balance = 5000.0
total_deposits = 0.0
total_withdrawals = 0.0
transaction_count = 0

MIN_DEPOSIT = 100
MAX_DEPOSIT = 50000
MIN_WITHDRAWAL = 100
MAX_WITHDRAWAL = 10000
MIN_BALANCE = 500

while True:
    print("\n===== ATM MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance Inquiry")
    print("4. Transaction Summary")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter deposit amount: "))

            if MIN_DEPOSIT <= amount <= MAX_DEPOSIT:
                balance += amount
                total_deposits += amount
                transaction_count += 1
                print("Deposit successful!")
                print(f"Current balance: Rs. {balance:.2f}")
            else:
                print("Invalid deposit amount!")
                print(f"Deposit must be between Rs. {MIN_DEPOSIT} "
                      f"and Rs. {MAX_DEPOSIT}.")

        elif choice == 2:
            amount = float(input("Enter withdrawal amount: "))

            if not MIN_WITHDRAWAL <= amount <= MAX_WITHDRAWAL:
                print("Invalid withdrawal amount!")
                print(f"Withdrawal must be between Rs. "
                      f"{MIN_WITHDRAWAL} and Rs. {MAX_WITHDRAWAL}.")

            elif balance - amount < MIN_BALANCE:
                print("Insufficient funds!")
                print(f"Minimum balance of Rs. {MIN_BALANCE} "
                      "must be maintained.")

            else:
                balance -= amount
                total_withdrawals += amount
                transaction_count += 1
                print("Withdrawal successful!")
                print(f"Current balance: Rs. {balance:.2f}")

        elif choice == 3:
            print(f"Current account balance: Rs. {balance:.2f}")

        elif choice == 4:
            print("\n===== TRANSACTION SUMMARY =====")
            print(f"Total deposits: Rs. {total_deposits:.2f}")
            print(f"Total withdrawals: Rs. {total_withdrawals:.2f}")
            print(f"Total transactions: {transaction_count}")
            print(f"Current balance: Rs. {balance:.2f}")

        elif choice == 5:
            print("Thank you for using our ATM!")
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please select 1 to 5.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")
