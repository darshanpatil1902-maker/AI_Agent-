print("Simple AI Agent")
print("Type 'exit' to stop.\n")

while True:

    question = input("You: ").lower()

    if question == "exit":
        print("Agent: Goodbye!")
        break

    if "hello" in question or "hi" in question:
        print("Agent: Hello! How can I help you?")

    elif "name" in question:
        print("Agent: I am a simple AI agent.")

    elif "python" in question:
        print("Agent: Python is a popular programming language.")

    elif "ai" in question or "artificial intelligence" in question:
        print(
            "Agent: Artificial Intelligence is technology "
            "that enables computers to perform tasks that "
            "normally require human intelligence."
        )

    elif "machine learning" in question:
        print(
            "Agent: Machine Learning is a branch of AI that "
            "allows computers to learn patterns from data."
        )

    elif "who are you" in question:
        print("Agent: I am a simple Python-based AI agent.")

    elif "help" in question:
        print(
            "Agent: You can ask me about AI, Python, "
            "Machine Learning, or say hello."
        )

    else:
        print("Agent: I don't know the answer yet.")
