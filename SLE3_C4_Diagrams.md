# SLE-3 C4 Model Diagrams

**Project:** Simple AI Agent / Study Buddy Agent  
**PRN:** 25UAM056  
**Name:** Darshan Rajendra Patil

> These diagrams use Mermaid and can be rendered by GitHub.

## Level 1 – Context Diagram

~~~mermaid
flowchart LR
    U[User] -->|Enters question / command| A[Simple AI Agent]
    A -->|Displays response| U
~~~

### Explanation
The User communicates directly with the Simple AI Agent through the terminal. The agent receives the question, processes it using its rules, and returns a response.

## Level 2 – Container Diagram

~~~mermaid
flowchart LR
    U[User] --> UI[Terminal User Interface]
    UI --> IH[Input Handler]
    IH --> RE[Response Engine]
    RE --> KR[Knowledge / Response Rules]
    RE --> SC[Session Controller]
    SC --> UI
    UI --> U
~~~

### Container Responsibilities
| Container | Responsibility |
|---|---|
| Terminal User Interface | Accepts input and displays responses |
| Input Handler | Reads input and converts it to lowercase |
| Response Engine | Checks keyword-based conditions |
| Knowledge / Response Rules | Provides predefined responses |
| Session Controller | Controls repeated interaction and exit |

## Level 3 – Component Diagram

### Components inside the Response Engine

~~~mermaid
flowchart TD
    RE[Response Engine]
    RE --> GM[Greeting Matcher]
    RE --> TM[Topic Matcher]
    RE --> IM[Identity Matcher]
    RE --> HM[Help Matcher]
    RE --> DR[Default Response Handler]
    GM --> GR[Greeting Response]
    TM --> TR[AI / Python / ML Response]
    IM --> IR[Identity Response]
    HM --> HR[Help Response]
    DR --> UR[Unknown Request Response]
~~~

### Explanation
The Response Engine is the main decision-making part of the agent. It checks the user's text against keyword conditions. If a match is found, the corresponding predefined response is returned; otherwise, the default response is used.

## Level 4 – Code Level Overview

~~~text
Agent.py
|
+-- input('You: ')              -> Read user question
+-- question.lower()            -> Normalize input
+-- if / elif conditions        -> Match keywords
+-- Greeting conditions         -> hello, hi
+-- Topic conditions            -> python, ai, machine learning
+-- Identity / help conditions  -> name, who are you, help
+-- exit condition              -> Stop the program
+-- else                        -> Unknown response
~~~

### Main Code Responsibilities
- **Input:** Reads the question from the terminal.
- **Normalization:** Converts the question to lowercase.
- **Decision:** Uses sequential if/elif keyword matching.
- **Response:** Prints the matching predefined answer.
- **Control:** Continues until the user enters exit.