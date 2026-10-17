# SLE-4: Final Viva & Architecture Decision Record (ADR)

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**PRN:** 25UAM056  
**Name:** Darshan Rajendra Patil  
**Division:** A  
**Date:** 17 October 2026

## PART A: Architecture Decision Record (ADR)

**Title:** Use of Sequential Keyword-Matching Rules in the Simple AI Agent  
**Status:** Accepted

### 1. Context
The project is a beginner-friendly Python agent that runs in a terminal and responds to user questions. The documented design uses keywords and simple rules to choose a response. The system is intended to be easy to run locally and straightforward to explain and maintain. The important design question is how the agent should identify a user's topic and select a response.

### 2. Decision
Use an ordered set of keyword-matching rules to select a response. Keep input handling, response matching, and output/session handling as separate logical responsibilities so the program remains understandable and testable.

### 3. Alternatives Considered
- **Machine-learning intent classifier:** may understand more varied wording, but requires training examples and adds complexity.
- **Exact-match response list:** simple, but often fails when the same question is phrased differently.
- **External LLM/API:** can provide richer responses, but depends on network access, credentials, and an external service.

### 4. Rationale / Justification
- Keyword rules fit the documented scope of a small, local, beginner-friendly terminal agent.
- The approach can be implemented with standard Python and does not require an additional machine-learning package or API.
- The matching process is transparent: the input is checked against rules and a response is selected.
- Separating input, matching, and output responsibilities is consistent with the component-based explanation used in the SLE-3 C4 model.
- Individual rules can be edited and tested without retraining a model.
- The trade-off is reduced flexibility for synonyms, spelling errors, and unfamiliar sentence structures.

**SLE-2 evidence to complete:** The actual SLE-2 profiling report and its measured runtime/memory values were not available in the materials reviewed for this report. Add the real measurements and test/input size before final submission; no figures have been invented.

### 5. Consequences

**Positive**
- Easy to understand, run, debug, and explain during viva.
- Works locally without an external API or internet connection.
- Predictable responses for recognized keywords.

**Negative / Trade-offs**
- May miss synonyms, spelling mistakes, or questions outside the rules.
- Rule order can matter when multiple keyword groups match.
- The rules become harder to maintain as the number of supported topics increases.

**References**
- Repository: https://github.com/darshanpatil1902-maker/AI_Agent-
- Add the exact SLE-2 profiling report and SLE-3 C4 diagram filenames or links.

## PART B: Short Summary of My SLE Journey
SLE-1 focused on building the agent/search code and documenting the project. SLE-2 involved profiling the code and comparing its performance. SLE-3 described the architecture through C4 Context, Container, Component, and Code diagrams. In SLE-4, this ADR records the reason for using sequential keyword matching and explains its alternatives and trade-offs. Check the SLE-2 figures and SLE-3 diagram details against the original submitted files.

## PART C: AI Contribution Note
- **AI tool used:** ChatGPT.
- **What AI helped with:** Organizing the ADR, explaining alternatives and trade-offs, and preparing the report structure.
- **What I will do myself:** Verify the decision against the actual source code, insert the real SLE-2 profiling results, and ensure the SLE-3 references match the submitted diagrams.

## PART D: Viva Preparation Notes
- Explain why keyword matching suits the current project and name at least two alternatives.
- State the actual SLE-2 profiling measurements and what they show.
- Explain the Context, Container, Component, and Code diagrams from the submitted SLE-3 work.
- Describe the main limitation of keyword matching and how the design could be improved if the project grows.

> **Submission reminder:** The SLE-4 guideline asks for a 2–3 page report (maximum 4 pages) and specifically expects SLE-2 profiling evidence. Add the actual numbers before final submission.
