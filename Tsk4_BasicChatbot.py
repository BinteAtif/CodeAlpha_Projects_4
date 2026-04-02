def chatbot():
    print("Welcome to the Basic Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I don't understand that. Please say 'hello', 'how are you', or 'bye'.")

# Run the chatbot
chatbot()