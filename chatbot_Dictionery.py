print("Welcome to Decode Bot!")
print("Type 'exit' to end the conversation.")

responses = {
    "hello": "Hi there! ",
    "hi": "Hello! How can I help you?",
    "hey": "Hey! Nice to meet you.",
    "how are you": "I'm doing great! Thanks for asking.",
    "what is your name": "My name is Decode Bot.",
    "who made you": "I was created by a Python programmer.",
    "which language were you developed in": "I was developed using Python.",
    "what is your favourite colour": "I like Red.",
    "what can you do": "I can answer simple predefined questions.",
    "thank you": "You're welcome!",
    "thanks": "Happy to help!",
    "good morning": "Good Morning! Have a wonderful day.",
    "good afternoon": "Good Afternoon!",
    "good evening": "Good Evening!",
    "bye": "Goodbye! Have a nice day."
}

while True:
    user = input("\nYou: ").lower().strip()

    if user == "exit":
        print("Bot: Goodbye! Have a nice day.")
        break

    reply = responses.get(
        user,
        "Sorry, I don't understand that. Please try another question."
    )

    print("Bot:", reply)
