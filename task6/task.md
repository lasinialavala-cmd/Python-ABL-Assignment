# Problem Statement
Develop a Traffic Flow and Congestion Analysis System that processes vehicle counts collected from multiple roads at different time intervals. The system should analyze traffic patterns, identify peak traffic periods, classify congestion levels, and detect roads where vehicle counts exceed their capacity thresholds.

The program should:
- Accept the number of roads and time intervals.
- Record the number of vehicles observed on each road during each interval.
- Calculate total and average traffic for every road.
- Identify the peak traffic period for each road and across all roads.
- Classify congestion as Low, Moderate, High, or Severe.
- Identify roads whose vehicle counts exceed their predefined capacity.
- Display a summary report with traffic statistics and congestion warnings.
Example classification rules:
Vehicles per interval	Congestion level
0–20% of capacity	Low
Above 20–50%	Moderate
Above 50–80%	High
Above 80%	Severe

A road is flagged as over capacity when its vehicle count exceeds its specified capacity for an interval. These thresholds are illustrative and should be adjusted to suit the traffic model being used.
# Algorithm
1. Start.
2. Input the number of roads and time intervals.
3. For each road, enter its name and vehicle capacity per interval.
4. Record the vehicle count for every time interval.
5. Validate that capacity is positive and vehicle counts are non-negative.
6. Calculate the total and average vehicle count for each road.
7. Identify the interval with the highest vehicle count for each road.
8. Calculate the total traffic for each interval across all roads.
9. Identify the overall peak traffic interval.
10. Calculate congestion percentage using:
\[
\text{Congestion Percentage}
= \frac{\text{Vehicle Count}}{\text{Road Capacity}}\times100
\]

11. Classify congestion using the predefined thresholds.
12. Flag roads whose vehicle counts exceed their capacity.
13. Display the traffic analysis report.
14. Stop.
15. ```mermaid
    
flowchart TD
    A([Start]) --> B[/Input number of roads and intervals/]
    B --> C[/Enter road name and capacity/]
    C --> D[/Enter vehicle counts for each interval/]
    D --> E{Valid non-negative counts?}
    E -->|No| F[Re-enter invalid count]
    F --> D
    E -->|Yes| G[Calculate total and average traffic]
    G --> H[Find peak interval for each road]
    H --> I[Calculate congestion percentage]
    I --> J{Congestion percentage}
    J -->|0 to 20%| K[Low]
    J -->|Above 20 to 50%| L[Moderate]
    J -->|Above 50 to 80%| M[High]
    J -->|Above 80%| N[Severe]
    K --> O{Count exceeds capacity?}
    L --> O
    M --> O
    N --> O
    O -->|Yes| P[Flag road as over capacity]
    O -->|No| Q[Record traffic status]
    P --> R{More roads?}
    Q --> R
    R -->|Yes| C
    R -->|No| S[Find overall peak traffic interval]
    S --> T[Display traffic analysis report]
    T --> U([Stop])
```
# Sample Input
Assume the system monitors three roads over three time intervals: Morning, Afternoon, and Evening.
Enter number of roads: 3
Enter number of time intervals: 3

Road 1 name: Main Road
Capacity per interval: 100
Morning vehicles: 40
Afternoon vehicles: 65
Evening vehicles: 95

Road 2 name: Market Road
Capacity per interval: 80
Morning vehicles: 30
Afternoon vehicles: 75
Evening vehicles: 90

Road 3 name: Highway
Capacity per interval: 200
Morning vehicles: 100
Afternoon vehicles: 120
Evening vehicles: 150


# Sample Output
========== TRAFFIC ANALYSIS REPORT ==========

Road: Main Road
Total vehicles: 200
Average vehicles per interval: 66.67
Peak period: Evening (95 vehicles)
Congestion: Severe
Over capacity: No

Road: Market Road
Total vehicles: 195
Average vehicles per interval: 65.00
Peak period: Evening (90 vehicles)
Congestion: Severe
Over capacity: Yes

Road: Highway
Total vehicles: 370
Average vehicles per interval: 123.33
Peak period: Evening (150 vehicles)
Congestion: High
Over capacity: No

========== OVERALL ANALYSIS ==========

Morning total: 170 vehicles
Afternoon total: 260 vehicles
Evening total: 335 vehicles

Overall peak period: Evening
Total vehicles during peak: 335

Roads exceeding capacity:
Market Road - Evening (90 / 80 vehicles)

Analysis completed.

