import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ELEVENLABS_API_KEY")
voice_id = os.getenv("ELEVENLABS_VOICE_ID")
url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
headers = {
    "xi-api-key": api_key,
    "Content-Type": "application/json"
}
payload = {
    "text": "Yes, he does. In fact he's been working on a new project that involves integrating AI into their existing systems, but rather wishes he spends time with you instead. He has been thinking about you a lot lately",
    "model_id": "eleven_multilingual_v2"
}

response = requests.post(url, json=payload, headers=headers)
print(f"Status: {response.status_code}")

if response.status_code == 200:
    with open("output.mp3", "wb") as f:
        f.write(response.content)
        print("Audio saved to output.mp3")
    
else:
    print(response.json())


