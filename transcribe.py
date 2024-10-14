import openai
from openai import OpenAI
import os

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

def audio_transcribe(filename):
    # Set your API key
    APIkey= os.getenv('OPENAI_API_KEY')
    client = OpenAI()
    print("Transcription completed")
    with open(filename, 'rb') as audio_file:
      response = client.audio.transcriptions.create(
          model="whisper-1",
          file=audio_file,
          response_format="json"  # Ensure response is in JSON format
      )
    print("Transcription completed")
    try:
      result = response
      print("TRANSCRIBE:", result)
      return result
    except KeyError:
      print("Error: 'text' key not found in the response")
      return null