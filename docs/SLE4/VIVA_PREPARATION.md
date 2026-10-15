# SLE-4 Viva Preparation — Simple AI Agent

**Student:** Darshan Rajendra Patil  
**PRN:** 25UAM056 | **Division:** A  
**Course:** 02AML204 – Introduction to Artificial Intelligence

## Short answers to practise

### 1. What is the main architecture decision?
I chose sequential keyword-matching rules because the project is a small, beginner-friendly Python agent that runs locally in the terminal. The rules are easy to understand, debug, and maintain.

### 2. What alternatives did you consider?
A machine-learning intent classifier, exact-match responses, and an external LLM/API. They can provide broader coverage or richer responses, but add complexity, brittleness, dependencies, or network/API requirements.

### 3. What is the main disadvantage of keyword matching?
It can miss a question if the user uses different wording, synonyms, or spelling mistakes. The rule order can also matter if several keywords match.

### 4. What did SLE-2 profiling show?
**Use your actual SLE-2 report to answer this.** State the test/input size and the measured runtime and memory figures, then explain what the comparison means. Do not guess or invent numbers.

### 5. Explain the C4 architecture in simple words.
- **Context:** shows the agent and the user/external actors around it.
- **Container:** shows the main runnable application and its interfaces.
- **Component:** breaks the application into responsibilities such as input handling, response matching, and output/session handling.
- **Code:** gives a lower-level view of implementation classes/functions or rule logic.
Use the exact names and boundaries shown in your submitted SLE-3 diagrams.

### 6. What happens if the project grows?
The rule list may become difficult to maintain, and keyword matching may become less accurate. I could separate rules into modules and add tests; if the requirements demand broader language understanding, I could evaluate an intent classifier using measured accuracy and resource costs.

### 7. What did AI contribute?
AI helped organize the ADR and prepare practice questions. I must verify the technical details against my own code, profiling report, and C4 diagrams, and make any needed corrections.

## Final checklist
- [ ] Know the actual SLE-2 runtime and memory results.
- [ ] Be able to explain the four C4 diagrams using the submitted versions.
- [ ] Verify the decision matches the current repository code.
- [ ] Add links to SLE-2 and SLE-3 deliverables.
- [ ] Explain both benefits and trade-offs in my own words.
