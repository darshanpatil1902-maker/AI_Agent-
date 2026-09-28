# SLE-2: Profiling Report

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**PRN:** 25UAM056  
**Name:** Darshan Rajendra Patil  
**Division:** A  
**Date:** 28/09/2026  

## 1. Algorithms / Versions Profiled

The AI agent repository contains a simple Study Buddy AI Agent.

Two versions of the response-selection logic were considered for profiling:

### Version 1 – If/Elif Based Response Selection

The agent checks the user command using a sequence of `if` and `elif` conditions.

Example:

- If the command is a greeting → return a greeting.
- If the command contains "study" → return a study response.
- If the command contains "python" → return a Python response.
- If the command contains "ai" → return an AI response.
- Otherwise → return a default response.

### Version 2 – Dictionary Based Response Selection

The response selection is implemented using a Python dictionary.

The user command is used as a key to find the corresponding response.

This reduces the number of conditional checks required for direct keyword lookup.

---

## 2. Profiling Method

The two versions were tested using Python's `timeit` module.

The same test commands were used for both versions:

- hello
- help
- study
- python
- ai
- bye
- unknown command

Each test was executed **10,000 times**.

Three runs were taken for each version and the average execution time was calculated.

Memory usage was also checked using Python's `tracemalloc` module.

The main parameters considered were:

1. Execution time
2. Average execution time
3. Memory usage
4. Response-selection method

---

## 3. Results

| Version | Run 1 (sec) | Run 2 (sec) | Run 3 (sec) | Mean Time (sec) | Peak Memory |
|---|---:|---:|---:|---:|---:|
| If/Elif | 0.014830 | 0.012642 | 0.013586 | 0.013686 | 56,064 bytes |
| Dictionary | 0.009937 | 0.010256 | 0.013125 | 0.011106 | 56,064 bytes |

### Performance Ratio

The dictionary-based version required approximately:

**0.013686 / 0.011106 ≈ 1.23**

Therefore, in this test, the dictionary-based approach was approximately **1.23 times faster** than the If/Elif version.

---

## 4. Observation

The profiling results show that the dictionary-based response selection completed the test in less average time than the If/Elif-based approach.

The memory usage was approximately the same for both versions in the measured test.

The difference in execution time is small because the AI agent is a small program with only a limited number of commands.

For a larger number of commands, dictionary-based lookup can become more useful because direct key lookup avoids checking a long sequence of conditions.

---

## 5. Justification and Analysis

The If/Elif approach checks conditions one after another until a matching condition is found.

Therefore, as the number of conditions increases, more comparisons may be required.

The dictionary approach stores responses using keys and performs direct lookup.

For this reason, dictionary-based response selection is more suitable when the number of fixed commands increases.

However, the measured result depends on the system and execution environment. Therefore, the profiling values represent the test environment used for this SLE-2 experiment.

The result supports the observation that the dictionary version had lower average execution time in the performed test.

---

## 6. AI Contribution Note

AI tools were used during the development and documentation process to understand the profiling concept, improve code structure, and prepare the report.

The final code and profiling results were reviewed and understood before including them in the project.

The student is responsible for understanding the implementation and the reported results.

---

## 7. Conclusion

The profiling experiment compared two response-selection approaches used in the AI Study Buddy Agent.

The measured results showed that the dictionary-based approach had a lower average execution time than the If/Elif approach, while memory usage remained approximately the same.

The experiment demonstrates how profiling can be used to compare different implementations using actual execution measurements rather than only theoretical assumptions.
