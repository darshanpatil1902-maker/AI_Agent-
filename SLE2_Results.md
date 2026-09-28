# SLE-2 Results

## Student Details

**Name:** Darshan Rajendra Patil  
**PRN:** 25UAM056  
**Division:** A  
**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Date:** 28/09/2026  

---

## Profiling Summary

Two response-selection implementations of the Study Buddy AI Agent were compared:

1. If/Elif based response selection
2. Dictionary based response selection

The same commands and test conditions were used for both versions.

Each version was tested for 10,000 iterations and three runs were recorded.

---

## Execution Time

### If/Elif Version

- Run 1: 0.014830 seconds
- Run 2: 0.012642 seconds
- Run 3: 0.013586 seconds
- Mean: 0.013686 seconds

### Dictionary Version

- Run 1: 0.009937 seconds
- Run 2: 0.010256 seconds
- Run 3: 0.013125 seconds
- Mean: 0.011106 seconds

---

## Comparison

The average execution time of the dictionary-based version was lower than the If/Elif version.

Approximate ratio:

`0.013686 / 0.011106 = 1.23`

Therefore, the dictionary version completed the measured workload in approximately 1.23 times less time.

---

## Memory

The measured peak memory usage was:

**56,064 bytes**

for both versions.

Therefore, no meaningful memory difference was observed in this test.

---

## Final Observation

The dictionary-based implementation showed better measured execution time for the selected test cases.

The difference is relatively small because the Study Buddy Agent contains only a small number of commands.

The profiling experiment demonstrates the importance of measuring actual program performance using tools such as `timeit` and `tracemalloc`.
