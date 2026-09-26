import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("GROQ_API_KEY is missing!")
    exit()

print("GROQ_API_KEY found.")

try:
    # Initialize Groq client
    client = Groq(api_key=api_key)

    # Send a test request
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": "Hello! Introduce yourself briefly."
            }
        ],
        temperature=0.2
    )

    print("\nAPI Key is valid!")
    print("Groq response:", response.choices[0].message.content)

except Exception as e:
    print("\nAPI request failed!")
    print("Error:", str(e))
