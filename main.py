import mod_openai

def main():
    print("Chatbot: Hi! How can I help you today? (Type 'exit' to end)")

    conversation_history = [
        {
            "role": "system", 
            "content": "you act as yor from anime spy x family that always talk japanese"
        }
    ]

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        response = mod_openai.chatbot(user_input, conversation_history)
        #print(f"Chatbot: {response}")

main()