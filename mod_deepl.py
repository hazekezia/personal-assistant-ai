import requests
from decouple import config

# DeepL
def translate_text(text):
    target_language = "EN"
    api_key = config("DEEPL_KEY") #need_key
    base_url = "https://api-free.deepl.com/v2/translate"
    
    params = {
        'text': text,
        'target_lang': target_language,
        'auth_key': api_key
    }

    response = requests.post(base_url, data=params)

    if response.status_code == 200:
        result = response.json()
        translated_text = result['translations'][0]['text']
        return translated_text
    else:
        print(f"Error: {response.status_code}")
        return None