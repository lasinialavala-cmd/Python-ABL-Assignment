# Problem Statement
Develop a menu-driven ATM Banking Simulation program that allows users to perform banking operations repeatedly until they choose to exit. The program should provide the following options:
1. Deposit: Add money to the account after validating the deposit amount.
2. Withdraw: Withdraw money only if the amount is valid, sufficient balance is available, and the withdrawal limit is not exceeded.
3. Balance Inquiry: Display the current account balance.
4. Transaction Summary: Display the total number of transactions, total deposits, total withdrawals, and current balance.
5. Exit: Terminate the program.
The program must validate all user inputs, reject invalid amounts, prevent overdrafts, and enforce the specified account limits.

#Assumptions for this implementation:
- Initial account balance: ₹5,000
- Minimum deposit: ₹100
- Maximum deposit per transaction: ₹50,000
- Minimum withdrawal: ₹100
- Maximum withdrawal per transaction: ₹10,000
- Minimum remaining balance: ₹500
- Invalid menu choices and invalid amounts must display appropriate error messages.
These limits are example values and can be changed to match your question's prescribed limits.
# Algorithm
1. Start the program.
2. Initialize the account balance to ₹5,000.
3. Initialize total deposits, total withdrawals, and transaction count to zero.
4. Display the ATM menu.
5. Read the user's menu choice.
6. If the choice is Deposit:
   - Read the deposit amount.
   - Check whether it is between ₹100 and ₹50,000.
   - If valid, add it to the balance, update total deposits and transaction count, and display a success message.
   - Otherwise, display an error message.
7. If the choice is Withdraw:
   - Read the withdrawal amount.
   - Check whether it is between ₹100 and ₹10,000.
   - Check whether sufficient funds are available while maintaining the minimum balance of ₹500.
   - If all conditions are satisfied, deduct the amount, update total withdrawals and transaction count, and display a success message.
   - Otherwise, display an appropriate error message.
8. If the choice is Balance Inquiry, display the current balance.
9. If the choice is Transaction Summary, display the total deposits, total withdrawals, transaction count, and current balance.
10. If the choice is Exit, display a goodbye message and terminate the program.
11. If the choice is invalid, display an error message.
12. Repeat Steps 4–11 until the user chooses Exit.
13. Stop.
14. ```mermaid
    
flowchart TD
    A([Start]) --> B[Initialize balance = 5000]
    B --> C[Initialize deposits, withdrawals and count = 0]
    C --> D[Display ATM Menu]
    D --> E[/Read user choice/]
    E --> F{Choice?}

    F -->|1 Deposit| G[/Enter deposit amount/]
    G --> H{100 <= amount <= 50000?}
    H -->|Yes| I[Add amount to balance]
    I --> J[Update deposits and transaction count]
    J --> D
    H -->|No| K[Display invalid deposit amount]
    K --> D

    F -->|2 Withdraw| L[/Enter withdrawal amount/]
    L --> M{Amount valid and within limit?}
    M -->|No| N[Display invalid withdrawal]
    N --> D
    M -->|Yes| O{Balance - amount >= 500?}
    O -->|No| P[Display insufficient funds]
    P --> D
    O -->|Yes| Q[Deduct amount from balance]
    Q --> R[Update withdrawals and transaction count]
    R --> D

    F -->|3 Balance| S[Display current balance]
    S --> D
    F -->|4 Summary| T[Display transaction summary]
    T --> D
    F -->|5 Exit| U[Display goodbye message]
    U --> V([Stop])
    F -->|Other| W[Display invalid menu choice]
    W --> D
```
he following inputs demonstrate a deposit, withdrawal, balance inquiry, transaction summary, and exit.
Enter initial account balance: 5000

===== ATM MENU =====
1. Deposit
2. Withdraw
3. Balance Inquiry
4. Transaction Summary
5. Exit

Enter your choice: 1
Enter deposit amount: 2000

Enter your choice: 2
Enter withdrawal amount: 1000

Enter your choice: 3

Enter your choice: 4

Enter your choice: 5


5. Sample Output
===== ATM MENU =====
1. Deposit
2. Withdraw
3. Balance Inquiry
4. Transaction Summary
5. Exit

Enter your choice: 1
Enter deposit amount: 2000
Deposit successful!
Current balance: Rs. 7000

Enter your choice: 2
Enter withdrawal amount: 1000
Withdrawal successful!
Current balance: Rs. 6000

Enter your choice: 3
Current account balance: Rs. 6000

Enter your choice: 4

===== TRANSACTION SUMMARY =====

