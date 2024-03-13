import os
import requests
from decouple import config

# TTS
def text_to_speech(text):
    url = config("EL_URL") #need_key
    output_file = "output.mp3"

    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "languages_id":"ja",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.3,
            "use_speaker_boost": True
        }
    }
    headers = {
        "xi-api-key": config("EL_API_KEY"), #need_key
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    if response.status_code == 200:
        with open(output_file, 'wb') as f:
            f.write(response.content)
        print(f"Playing audio.")
        os.system("start output.mp3")
    else:
        print(f"Error: {response.status_code} - {response.text}")