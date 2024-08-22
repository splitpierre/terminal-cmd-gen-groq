#!/usr/bin/env python3

from groq import Groq
import subprocess
import sys
from config import GROQ_API, MODEL

# Initialize the Groq client with the API key
client = Groq(api_key=GROQ_API)

def generate_command(task_description):
    # Send the request to the Groq API to generate a command
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an expert terminal commands for unix."+
                " Your task is to generate accurate and efficient terminal commands based on user input. Do not wrap the response command in quotes." +
                " DO NOT explain anything, the response should only be either a single command or an explanation on why its not possible.",
            },
            {
                "role": "user",
                "content": task_description,
            }
        ],
        model=MODEL,
    )
    # Extract the command from the API response
    command = response.choices[0].message.content
    return command

def copy_to_clipboard(command):
    # Copy the command to the clipboard using xclip
    process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
    process.communicate(command.encode('utf-8'))

if __name__ == "__main__":
    # Prompt the user to enter the task description
    if len(sys.argv) > 1:
        # Join all arguments into a single string to form the task description
        task_description = " ".join(sys.argv[1:])
    else:
        # Prompt the user to enter the task description
        task_description = input("Enter the task description for the command: ")
    

    # Generate the command based on the task description
    command = generate_command(task_description)
    
    # Print the generated command
    print(f"Generated Command:\n {command}")
    
    # Copy the command to the clipboard
    copy_to_clipboard(command)
    print("Command copied to clipboard. You can paste it into your terminal with Ctrl + Shift + V.")
