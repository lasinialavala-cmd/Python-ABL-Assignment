# Problem Statement
Design and implement an Employee Payroll and Deduction Analysis System that calculates employees' gross salary, deductions, and net salary based on their basic pay, allowances, overtime, and incentives.

The system should:
- Accept employee details and basic salary.
- Calculate allowances such as House Rent Allowance (HRA) and Dearness Allowance (DA).
- Calculate overtime pay and incentives.
- Determine gross salary by adding basic pay, allowances, overtime, and incentives.
- Apply progressive deductions based on salary slabs.
- Calculate net salary after deductions.
- Generate a formatted salary statement for each employee.
- Analyze payroll information, including total gross salary, total deductions, and total net salary.
Example payroll rules used:
Component	Rule
Basic salary	Entered by the user
HRA	20% of basic salary
DA	10% of basic salary
Overtime	Overtime hours × hourly rate × 1.5
Incentive	Entered by the user
PF deduction	12% of basic salary
Progressive tax	Based on gross salary

Progressive tax slabs
Gross salary	Tax rate
First ₹20,000	0%
Next ₹30,000	5%
Next ₹50,000	10%
Above ₹1,00,000	20%

These are illustrative payroll rules for an academic program, not official tax or payroll regulations.
# Algorithm
1. Start.
2. Input the number of employees.
3. For each employee:
   - Input employee ID and name.
   - Input basic salary.
   - Input overtime hours and hourly rate.
   - Input incentive amount.
4. Calculate HRA = 20% of basic salary.
5. Calculate DA = 10% of basic salary.
6. Calculate overtime pay = overtime hours × hourly rate × 1.5.
7. Calculate gross salary:
   Gross Salary = Basic Salary + HRA + DA + Overtime Pay + Incentive
8. Calculate PF deduction = 12% of basic salary.
9. Calculate progressive tax using the salary slabs.
10. Calculate total deductions:
    Total Deductions = PF + Progressive Tax

11. Calculate net salary:

    Net Salary = Gross Salary − Total Deductions
12. Display the formatted salary statement.
13. Store employee payroll details.
14. After processing all employees, calculate total gross salary, total deductions, and total net salary.
15. Display the payroll summary.
16. Stop.
17. ```memaid
    
flowchart TD
    A([Start]) --> B[/Input number of employees/]
    B --> C[/Enter employee details/]
    C --> D[Input basic salary, overtime and incentive]
    D --> E[Calculate HRA and DA]
    E --> F[Calculate overtime pay]
    F --> G[Calculate gross salary]
    G --> H[Calculate PF deduction]
    H --> I[Calculate progressive tax]
    I --> J[Calculate total deductions]
    J --> K[Calculate net salary]
    K --> L[Display salary statement]
    L --> M{More employees?}
    M -->|Yes| C
    M -->|No| N[Calculate payroll totals]
    N --> O[Display payroll summary]
    O --> P([Stop])
```
Enter number of months: 3

Month 1 consumption: 100
Month 2 consumption: 200
Month 3 consumption: 400


5. Sample Output
===== ELECTRICITY BILLING REPORT =====

Month 1
Consumption: 100 units
Energy Charges: Rs. 150.00
Fixed Charges: Rs. 100.00
Surcharge: Rs. 0.00
Rebate: Rs. 7.50
Final Bill: Rs. 242.50

Month 2
Consumption: 200 units
Energy Charges: Rs. 400.00
Fixed Charges: Rs. 100.00
Surcharge: Rs. 0.00
Rebate: Rs. 0.00
Final Bill: Rs. 500.00
Change from previous bill: 106.19%
WARNING: Unusual increase detected!

Month 3
Consumption: 400 units
Energy Charges: Rs. 1100.00
Fixed Charges: Rs. 100.00
Surcharge: Rs. 55.00
Rebate: Rs. 0.00
Final Bill: Rs. 1255.00
Change from previous bill: 151.00%
WARNING: Unusual increase detected!

===== SUMMARY =====
Total Bills: Rs. 1997.50
Average Monthly Bill: Rs. 665.83
Unusual Increases: 2


6. Python Code
# Progressive Electricity Billing SystemFIXED_CHARGE = 100UNUSUAL_INCREASE = 30  # Percentagedef calculate_energy_charges(units):    charges = 0    # First 100 units    charges += min(units, 100) * 1.50    # Units from 101 to 200    if units > 100:        charges += min(units - 100, 100) * 2.50    # Units from 201 to 500    if units > 200:        charges += min(units - 200, 300) * 4.00    # Units above 500    if units > 500:        charges += (units - 500) * 6.00    return chargesdef calculate_bill(units):    energy = calculate_energy_charges(units)    fixed = FIXED_CHARGE    surcharge = 0    rebate = 0    if units > 300:        surcharge = energy * 0.05



Result: The program calculates electricity bills using progressive consumption slabs, applies fixed charges, surcharges and rebates, and identifies month-to-month bill increases exceeding 30%.
















4. Employee Payroll and Deduction Analysis: Calculate gross salary from basic pay, allowances, overtime, and incentives; apply progressive deductions and generate a formatted salary statement.













4. Employee Payroll and Deduction Analysis
1. Problem Statement
Design and implement an Employee Payroll and Deduction Analysis System that calculates employees' gross salary, deductions, and net salary based on their basic pay, allowances, overtime, and incentives.

The system should:
- Accept employee details and basic salary.
- Calculate allowances such as House Rent Allowance (HRA) and Dearness Allowance (DA).
- Calculate overtime pay and incentives.
- Determine gross salary by adding basic pay, allowances, overtime, and incentives.
- Apply progressive deductions based on salary slabs.
- Calculate net salary after deductions.
- Generate a formatted salary statement for each employee.
- Analyze payroll information, including total gross salary, total deductions, and total net salary.
Example payroll rules used:
Component	Rule
Basic salary	Entered by the user
HRA	20% of basic salary
DA	10% of basic salary
Overtime	Overtime hours × hourly rate × 1.5
Incentive	Entered by the user
PF deduction	12% of basic salary
Progressive tax	Based on gross salary

Progressive tax slabs
Gross salary	Tax rate
First ₹20,000	0%
Next ₹30,000	5%
Next ₹50,000	10%
Above ₹1,00,000	20%

These are illustrative payroll rules for an academic program, not official tax or payroll regulations.
2. Algorithm
1. Start.
2. Input the number of employees.
3. For each employee:
   - Input employee ID and name.
   - Input basic salary.
   - Input overtime hours and hourly rate.
   - Input incentive amount.
4. Calculate HRA = 20% of basic salary.
5. Calculate DA = 10% of basic salary.
6. Calculate overtime pay = overtime hours × hourly rate × 1.5.
7. Calculate gross salary:
   Gross Salary = Basic Salary + HRA + DA + Overtime Pay + Incentive
8. Calculate PF deduction = 12% of basic salary.
9. Calculate progressive tax using the salary slabs.
10. Calculate total deductions:
    Total Deductions = PF + Progressive Tax

11. Calculate net salary:

    Net Salary = Gross Salary − Total Deductions
12. Display the formatted salary statement.
13. Store employee payroll details.
14. After processing all employees, calculate total gross salary, total deductions, and total net salary.
15. Display the payroll summary.
16. Stop.
3. Mermaid Flowchart
#chatgpt-mermaid-_r_ib_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-_r_ib_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_ib_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_ib_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-_r_ib_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-_r_ib_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-_r_ib_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-_r_ib_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-_r_ib_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-_r_ib_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-_r_ib_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-_r_ib_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_ib_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_ib_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-_r_ib_ p{margin:0;}#chatgpt-mermaid-_r_ib_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_ib_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-_r_ib_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_ib_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-_r_ib_ .label text,#chatgpt-mermaid-_r_ib_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_ib_ .node rect,#chatgpt-mermaid-_r_ib_ .node circle,#chatgpt-mermaid-_r_ib_ .node ellipse,#chatgpt-mermaid-_r_ib_ .node polygon,#chatgpt-mermaid-_r_ib_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-_r_ib_ .rough-node .label text,#chatgpt-mermaid-_r_ib_ .node .label text,#chatgpt-mermaid-_r_ib_ .image-shape .label,#chatgpt-mermaid-_r_ib_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-_r_ib_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-_r_ib_ .rough-node .label,#chatgpt-mermaid-_r_ib_ .node .label,#chatgpt-mermaid-_r_ib_ .image-shape .label,#chatgpt-mermaid-_r_ib_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-_r_ib_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-_r_ib_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_ib_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-_r_ib_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-_r_ib_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-_r_ib_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-_r_ib_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-_r_ib_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-_r_ib_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-_r_ib_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-_r_ib_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-_r_ib_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_ib_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-_r_ib_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-_r_ib_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-_r_ib_ .icon-shape,#chatgpt-mermaid-_r_ib_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-_r_ib_ .icon-shape p,#chatgpt-mermaid-_r_ib_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-_r_ib_ .icon-shape .label rect,#chatgpt-mermaid-_r_ib_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-_r_ib_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-_r_ib_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-_r_ib_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-_r_ib_ [data-look="neo"].node rect,#chatgpt-mermaid-_r_ib_ [data-look="neo"].cluster rect,#chatgpt-mermaid-_r_ib_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-_r_ib_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_ib_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-_r_ib_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-_r_ib_-gradient);stroke-width:1px;}#chatgpt-mermaid-_r_ib_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_ib_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-_r_ib_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-_r_ib_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_ib_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-_r_ib_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-_r_ib_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_ib_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-_r_ib_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_ib_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-_r_ib_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-_r_ib_ .node tspan[font-weight="normal"],#chatgpt-mermaid-_r_ib_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-_r_ib_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-_r_ib_ .node rect,#chatgpt-mermaid-_r_ib_ .node circle,#chatgpt-mermaid-_r_ib_ .node ellipse,#chatgpt-mermaid-_r_ib_ .node polygon,#chatgpt-mermaid-_r_ib_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-_r_ib_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-_r_ib_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-_r_ib_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-_r_ib_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_ib_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput number of employeesEnter employee detailsInput basic salary, overtimeand incentiveCalculate HRA and DACalculate overtime payCalculate gross salaryCalculate PF deductionCalculate progressive taxCalculate total deductionsCalculate net salaryDisplay salary statementMore employees?Calculate payroll totalsDisplay payroll summaryStopYesNo

# Sample Input
Enter number of employees: 2

Employee 1
Employee ID: 101
Employee Name: Ravi
Basic Salary: 40000
Overtime Hours: 10
Hourly Rate: 200
Incentive: 5000

Employee 2
Employee ID: 102
Employee Name: Priya
Basic Salary: 60000
Overtime Hours: 5
Hourly Rate: 300
Incentive: 8000


# Sample Output
========== EMPLOYEE SALARY STATEMENT ==========

Employee ID: 101
Employee Name: Ravi

Basic Salary:       Rs. 40000.00
HRA:                Rs. 8000.00
DA:                  Rs. 4000.00
Overtime Pay:         Rs. 3000.00
Incentive:            Rs. 5000.00

Gross Salary:        Rs. 60000.00
PF Deduction:         Rs. 4800.00
Progressive Tax:      Rs. 4000.00
Total Deductions:     Rs. 8800.00

Net Salary:          Rs. 51200.00

=============================================

========== EMPLOYEE SALARY STATEMENT ==========
