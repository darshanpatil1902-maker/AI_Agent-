# SLE-4 — Architecture Decision Record (ADR)

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Project:** Simple AI Agent  
**PRN:** 25UAM056  
**Name:** Darshan Rajendra Patil  
**Division:** A  
**Status:** Accepted  
**Date:** 15 October 2026  
**Repository:** https://github.com/darshanpatil1902-maker/AI_Agent-

## Title: Use Sequential Keyword-Matching Rules for the Simple AI Agent

### 1. Context
The project is a beginner-friendly Python agent that runs in a terminal and replies to user questions. The current project description says that it detects keywords and selects a response using simple decision-making rules. The design should remain easy to understand, run locally, and require no external libraries, API key, or internet connection. The decision therefore concerns how the agent routes each input to a suitable response.

### 2. Decision
Use a small, ordered set of keyword-matching rules to classify the user's message and return a response. Keep input handling, response matching, and output/session handling logically separated so that each part can be understood and tested independently.

### 3. Alternatives Considered
- **Machine-learning intent classifier:** Could generalize to more varied wording, but would add training data, dependencies, and complexity.
- **Large collection of exact-match responses:** Simple to implement, but is brittle when users phrase the same question differently.
- **External LLM/API service:** Could produce richer answers, but would require network access, an API credential, and external service availability.

### 4. Rationale / Justification
- Sequential keyword rules match the project's documented beginner-friendly, local-terminal scope.
- The approach uses standard Python and avoids installing additional packages.
- It is straightforward to explain during viva: input is checked against rules and the matching response is returned.
- It supports clear component boundaries for input handling, response matching, and output.
- Individual rules can be updated without introducing a model-training pipeline.
- The choice trades broad language understanding for transparency and low setup cost.
- **SLE-2 evidence to add before final submission:** insert the actual measured runtime, memory usage, and test/input size from the SLE-2 comparison report here. Those measurements were not available in the materials used to prepare this file, so no numbers have been invented.
- **SLE-3 link:** connect this rationale to the actual Context, Container, Component, and Code diagrams in the SLE-3 deliverable.

### 5. Consequences

**Positive**
- Easy to run, debug, explain, and modify.
- No external API, internet connection, or third-party package is required.
- The rules provide predictable responses for recognized keywords.

**Negative / Trade-offs**
- The agent may fail to understand synonyms, spelling mistakes, or unfamiliar phrasing.
- Rule order matters when a message matches more than one keyword group.
- As the number of topics grows, the rule set can become harder to maintain.
- The agent does not learn automatically from new conversations.

### 6. References
- Project repository: https://github.com/darshanpatil1902-maker/AI_Agent-
- SLE-2 profiling report: add the actual file/link and measured results.
- SLE-3 C4 diagrams: add the actual file/link.

## Part B — Short SLE Journey
- **SLE-1:** Built the Python agent and documented its purpose and usage.
- **SLE-2:** Profiled the implementation and compared results; add the actual measurements from that report to this ADR.
- **SLE-3:** Prepared C4 architecture diagrams to explain the system at different levels.
- **SLE-4:** Records why sequential keyword matching was selected and prepares a justification for viva.

## Part C — AI Contribution Note
- **AI tool used:** ChatGPT.
- **AI helped with:** Organizing the ADR, describing alternatives and trade-offs, and preparing viva prompts.
- **My work:** Review this document against my actual code, SLE-2 measurements, and SLE-3 diagrams; correct anything that does not match my submitted work before assessment.

> **Before submitting:** Replace the SLE-2 evidence note with your real profiling numbers and add links to the actual SLE-2/SLE-3 files. Do not present placeholder evidence as measured results.
