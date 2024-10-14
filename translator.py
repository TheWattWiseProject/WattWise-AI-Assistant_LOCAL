import openai
import os
import asyncio
import json

# Load environment variables from .env file
load_dotenv()

def fetch_thread_messages(thread_id):
    response = openai.Threads.messages.list(thread_id=thread_id)
    return response['data']

async def save_messages_to_file(messages, file_path):
  os.makedirs(os.path.dirname(file_path), exist_ok=True)
  with open(file_path, 'w') as file:
      json.dump(messages, file, indent=4)
  print(f"Messages saved to {file_path}")

async def main():
    thread_id = "thread_zkcCDDDreSQz9UmjgOonmpph"  # Replace with your actual thread ID
    # Initialize the OpenAI client
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # Replace with your actual API key
    client = openai.OpenAI(api_key=OPENAI_API_KEY)

    threadMessages = client.beta.threads.messages.list(
    "thread_KPjHC6XszjBWRFYWlOWIY7eh")

    print(threadMessages)
    save_path =  'docs/static2'
  
    file_name = f"{save_path}/thread_messages.json"
    await save_messages_to_file(threadMessages, file_name)
    
if __name__ == "__main__":
  asyncio.run(main())

