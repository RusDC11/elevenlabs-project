import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")

def get_voices():
    headers = {"xi-api-key": api_key}
    response = requests.get("https://api.elevenlabs.io/v1/voices", headers=headers)
    if response.status_code == 200:
        return response.json()["voices"]
    print(f"Error fetching voices: {response.status_code}")
    return []

def generate_audio(text, voice_id, filename):
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
            print(f"API Error {response.status_code}: {response.json()}")
    except requests.exceptions.ConnectionError:
        print("Error: No Internet Connection.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    print("ElevenLabs TTS Tool\n")

    voices = get_voices()
    if not voices:
        return
    
    print("Available voices.")
    for i, voice in enumerate(voices):
        print(f"{i + 1}. {voice['name']}")

    choice = int(input("\nSelect a voice number: ")) - 1
    selected_voice = voices[choice]
    print(f"Selected Voice: {selected_voice['name']}")

    print("\nEnter line of text. Type 'done' when finished: ")
    lines = []
    while True:
        line = input("> ")
        if line.lower() == "done":
            break
        lines.append(line)

    for i, line in enumerate(lines):
        filename = f"output_{i + 1}.mp3"
        print(f"Processing line {i + 1}...")
        generate_audio(line, selected_voice["voice_id"], filename)

    print("\nAll done.")

if __name__ == "__main__":
    main()