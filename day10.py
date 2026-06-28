import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")
voice_id = os.getenv("ELEVENLABS_VOICE_ID")

def generate_audio(text, filename):
    if not text.strip():
        print("Skipping empty line.")
        return
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Saved: {filename}")
        else:
            print(f"API Error {response.status_code} {response.json()}")
    except requests.exceptions.ConnectionError:
        print("Error: No internet connection.")
    except Exception as e:
        print(f"Unexpected error: {e}")

lines = [
     "Welcome to ElevenLabs. The future of voice AI starts here.",
    "This is line two of the batch. Each line becomes its own audio file.",
    "Batch processing complete. Thank you for listening."
]

for i, line in enumerate(lines):
    filename = f"batch_output_{i + 1}.mp3"
    print(f"Processing line {i + 1}: {line}")
    generate_audio(line, filename)