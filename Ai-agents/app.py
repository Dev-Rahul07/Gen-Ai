import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()

# funtions
def sum_numbers(a: int, b: int) -> dict:
    """Adds two numbers."""
    result = a + b
    print(f"Tool Call: sum_numbers({a}, {b})")
    return {"result": result}

def subtract_numbers(a: int, b: int) -> dict:
    """Subtracts two numbers."""
    result = a - b
    print(f"Tool Call: subtract_numbers({a}, {b})")
    return {"result": result}

def multiply_numbers(a: int, b: int) -> dict:
    """Multiplies two numbers."""
    result = a * b
    print(f"Tool Call: multiply_numbers({a}, {b})")
    return {"result": result}

def say_hello(name: str) -> dict:
    """Returns a greeting message."""
    message = f"Hello, {name}!"
    print(f"Tool Call: say_hello({name})")
    return {"message": message}

# Configure the client and model
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[sum_numbers, subtract_numbers, multiply_numbers, say_hello]
)



while True:
    userinput = input("Enter a command (or 'exit' to quit): ")
    if userinput.lower() == 'exit':
        break
# Make the request
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=userinput,
        config=config,
    )

# Print the final, user-facing response
    print(response.text)