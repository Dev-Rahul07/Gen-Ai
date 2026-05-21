from google import genai
from dotenv import load_dotenv
import os
load_dotenv()
client = genai.Client()
chat = client.chats.create(model="gemini-3-flash-preview")

history = []

while True:
    user_question = input("You: ")

    if user_question.lower() == "exit":
        break

    # Send message
    response = chat.send_message(user_question)

    # Store history (your own copy)
    history.append({"role": "user", "content": user_question})
    history.append({"role": "assistant", "content": response.text})

    # Print response
    print("Bot:", response.text)

print("\n--- Chat History (Your List) ---")
for msg in history:
    print(f"{msg['role']}: {msg['content']}")

print("\n--- Chat History (Model Context) ---")
for message in chat.get_history():
    print(f"{message.role}: {message.parts[0].text}")