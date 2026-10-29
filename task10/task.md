# Problem Statement
Develop a Python program to shortlist students for scholarships by applying multiple eligibility conditions, including minimum academic marks, attendance percentage, and family income. Eligible students are ranked according to specified rules, and scholarships are awarded to the highest-ranked candidates within a fixed quota.

Assumptions:
- Minimum academic aggregate: 75%.
- Minimum mark in each subject: 60%.
- Minimum attendance: 75%.
- Maximum annual family income: ₹3,00,000.
- Scholarship quota: 3 students.
- Ranking rules:
  1. Higher academic aggregate.
  2. Higher attendance percentage.
  3. Higher minimum subject mark.
  4. Lower annual family income.
# Algorithm
1. Start the program.
2. Input the scholarship quota and number of applicants.
3. For each applicant, enter name, subject marks, attendance percentage, and annual family income.
4. Calculate the academic aggregate.
5. Check academic, subject-wise, attendance, and income eligibility.
6. Separate eligible students from ineligible students.
7. Sort eligible students using the specified ranking rules.
8. Select candidates up to the available scholarship quota.
9. Display shortlisted candidates with their ranks and rejected candidates with reasons.
10. Stop.
    ```mermaid
    
flowchart TD
    A([Start]) --> B[Input applicants and scholarship quota]
    B --> C[Enter student marks, attendance and income]
    C --> D[Calculate academic aggregate]
    D --> E{Meets all eligibility criteria?}
    E -- No --> F[Record rejection reason]
    E -- Yes --> G[Add student to eligible list]
    F --> H{More applicants?}
    G --> H
    H -- Yes --> C
    H -- No --> I[Sort eligible students by ranking rules]
    I --> J[Select students up to scholarship quota]
    J --> K[Display shortlist and rejected candidates]
    K --> L([Stop])
```
. Sample Input
Enter scholarship quota: 3
Enter number of applicants: 5

Applicant 1
Student name: Asha
Subject 1: 90
Subject 2: 85
Subject 3: 88
Attendance percentage: 92
Annual family income: 200000

Applicant 2
Student name: Ravi
Subject 1: 80
Subject 2: 78
Subject 3: 82
Attendance percentage: 85
Annual family income: 250000

Applicant 3
Student name: Meena
Subject 1: 95
Subject 2: 92
Subject 3: 90
Attendance percentage: 90
Annual family income: 280000

Applicant 4
Student name: Kiran
Subject 1: 70
Subject 2: 65
Subject 3: 68
Attendance percentage: 80
Annual family income: 180000

Applicant 5
Student name: Divya
Subject 1: 85
Subject 2: 82
Subject 3: 80
Attendance percentage: 88
Annual family income: 350000


6. Sample Output
========== SCHOLARSHIP SHORTLIST ==========
Rank  Name                 Aggregate   Attendance        Income
---------------------------------------------------------------
1     Meena                   92.33%       90.00%     280000.00
2     Asha                    87.67%       92.00%     200000.00
3     Ravi                    80.00%       85.00%     250000.00

Scholarships awarded: 3 out of 3

========== REJECTED APPLICANTS ==========
Kiran: Aggregate below 75%
Divya: Family income exceeds Rs. 3,00,000
