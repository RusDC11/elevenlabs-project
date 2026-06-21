import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")
headers = {
    "xi-api-key":api_key
}
response = requests.get("https://api.elevenlabs.io/v1/voices",
headers=headers)
data = response.json()
for voice in data["voices"]:
    print(f"Name: {voice['name']} - ID: {voice['voice_id']}")