# Problem Statement
Develop a Python program to analyze manufacturing quality across multiple products and production batches. The program should record the total production quantity and number of defective units for each batch, calculate the defect percentage, classify batch quality, and identify batches that exceed the acceptable defect threshold.
2. Algorithm
1. Start the program.
2. Input the number of products and batches.
3. For each batch, enter the product name, batch number, production quantity, and defective units.
4. Validate that production quantity is positive and defective units are between zero and the production quantity.
5. Calculate the defect percentage using:
\[
\text{Defect Percentage}=
\frac{\text{Defective Units}}{\text{Production Quantity}}\times100
\]
#flowchat
1.start
7. Compare the defect percentage with the acceptable threshold of 5%.
8. Classify the batch as Acceptable if the defect percentage is at most 5%; otherwise, classify it as Needs Inspection.
9. Display the quality control matrix and list all batches exceeding the threshold.
10. Stop.
 ```mermaid

flowchart TD
    A([Start]) --> B[/Input number of batches/]
    B --> C[/Enter product, batch, production and defects/]
    C --> D{Is input valid?}
    D -- No --> E[/Display error and re-enter data/]
    E --> C
    D -- Yes --> F[Calculate defect percentage]
    F --> G{Defect percentage > 5%?}
    G -- Yes --> H[Mark Needs Inspection]
    G -- No --> I[Mark Acceptable]
    H --> J{More batches?}
    I --> J
    J -- Yes --> C
    J -- No --> K[Display quality control matrix]
    K --> L[Display batches exceeding threshold]
    L --> M([Stop])
```
5. Sample Input
Enter the number of batches: 3

Batch 1
Enter product name: Motor
Enter batch number: M101
Enter production quantity: 1000
Enter defective units: 30

Batch 2
Enter product name: Pump
Enter batch number: P201
Enter production quantity: 500
Enter defective units: 40

Batch 3
Enter product name: Valve
Enter batch number: V301
Enter production quantity: 800
Enter defective units: 20


6. Sample Output
========== QUALITY CONTROL MATRIX ==========
Product     Batch       Produced   Defects    Defect %  Status
---------------------------------------------------------------------------
Motor       M101            1000        30       3.00%  Acceptable
Pump        P201             500        40       8.00%  Needs Inspection
Valve       V301             800        20       2.50%  Acceptable

Batches Exceeding the 5% Defect Threshold:
Pump - Batch P201: 8.00% defects

Total units produced: 2300
Total defective units: 90
Overall defect percentage: 3.91%

    
