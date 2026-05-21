import os
import subprocess
from google import genai
from google.genai import types
from dotenv import load_dotenv
from click import command
load_dotenv()


system_prompt = """
You are MiniCursor, an AI coding assistant.

Rules:
- Help the user write code.
- Use tools whenever needed.
- Execute terminal commands carefully.
- Never run dangerous commands.
- Explain what you are doing before executing commands.
- Keep answers short and technical.
- my current os is: {os.name} 


-your job is to help the user write code and execute terminal commands.
- and give executable commands

-u can give  cmd like  -create a folder and file like insert all code the that respaced fil  and all
"""

# funtions
"""Funtion that excute any command"""
def run_command(command: str) -> dict:
    """
    Executes a terminal command and returns output.
    """

    print(f"\n[Executing]: {command}\n")

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        }

    except Exception as e:
        return {"error": str(e)}

# Configure the client and model
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[run_command],
    system_instruction=system_prompt
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