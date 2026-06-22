# ElevenLabs TTS Project

A Python integration with the ElevenLabs Text-to-Speech API, built as part of a 14-day self-study sprint targeting related roles.

## What id does

- Authenticates with the ElevenLabs API using a secure API key
- Fetches available voices from the ElevenLabs voice library
- Converts user-inputted text to speech using the Bella voice
- Saves the generated audi as an .mp3 file locally

## Tech stack

- Python 3.14
- ElevenLabs REST API
- requests library
- python-dotenv for secure credential management

## Setup

1. Clone this repository
2. Install dependencies: `pip install requests python-dotenv`
3. Create a `.env` file with your ElevenLabs API key:
    ELEVENLABS_API_KEY=your_key_here
    ELEVENLABS_VOICE_ID=your_voice_id_here
4. Run: `python day6.py`

## Files

- `day4.py` - Authenticated API call, fetches voice list
- `day5.py` - First TTS call, saves static audio output
- `day6.py` - User input driven TTS generation

## Author

Rusty - mechanical engineer with EDI experience transitioning into AI-adjacent technical roles