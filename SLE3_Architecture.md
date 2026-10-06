# SLE-3: Architectural Design (Full C4 Model)

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**PRN:** 25UAM056  
**Name:** Darshan Rajendra Patil  
**Division:** A  
**Date:** 06/10/2026  

## 1. System Title & Short Description

### Simple AI Agent / Study Buddy Agent

This beginner-friendly Python AI agent accepts questions through the terminal. It analyzes input using simple keyword-matching rules and selects a predefined response. It can respond to greetings and questions about AI, Python, Machine Learning, its identity, and help. It works locally without external libraries, APIs, or internet access.

## 2. Context Diagram – Level 1

See **SLE3_C4_Diagrams.md – Level 1**.

### Short Explanation
The user interacts with the Simple AI Agent through the terminal. The user enters a question or command, and the agent processes the text using its response rules. The selected response is displayed back to the user. The agent works locally and does not depend on external systems.

## 3. Container Diagram – Level 2

See **SLE3_C4_Diagrams.md – Level 2**.

### Containers
- **Terminal User Interface:** Accepts user input and displays the agent response.
- **Input Handler:** Reads the entered text and converts it to lowercase.
- **Response Engine:** Checks the input against sequential keyword-based conditions.
- **Knowledge / Response Rules:** Contains predefined responses for supported topics.
- **Session Controller:** Repeats interaction until the user enters exit.

## 4. Component Diagram – Level 3

### Main Container Selected: Response Engine
See **SLE3_C4_Diagrams.md – Level 3**.

### Components
- **Greeting Matcher:** Detects hello and hi.
- **Topic Matcher:** Detects python, ai, and machine learning.
- **Identity Matcher:** Handles questions about the agent identity.
- **Help Matcher:** Detects help requests.
- **Default Response Handler:** Gives a fallback response when no supported keyword is found.

The component structure represents the actual sequential if/elif response-selection logic used in Agent.py.

## 5. Code Level Overview – Level 4

- input('You: ') – accepts user input.
- question.lower() – normalizes input for matching.
- if/elif conditions – select a response based on keywords.
- Greeting matcher – handles hello and hi.
- Topic matchers – handle Python, AI and Machine Learning.
- help matcher – provides supported-query information.
- exit condition – terminates the session.
- else – returns an unknown-answer response.

## 6. Design Decisions

The architecture is kept simple because the project is a small rule-based AI agent. A separate response engine concept makes the decision-making responsibility clear, while the terminal handles user interaction. The design uses local keyword matching, so no external service or database is required.

## 7. AI Contribution Note

- **AI tools used:** ChatGPT
- **What AI helped with:** Understanding C4 architecture, organizing SLE-3 documentation, and preparing concise architecture descriptions.
- **What I did myself:** Reviewed the existing Python agent, selected the actual system structure, checked the code-level elements, and verified the final architecture.

## 8. Conclusion

The C4 model represents the Simple AI Agent from a high-level system view down to its code elements. The four levels show user interaction, major containers, response-engine components, and important Python code elements. This makes the system easier to understand, explain, and maintain.