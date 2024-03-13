from openai import OpenAI
import mod_deepl, mod_elevenlabs, mod_typing_effect
from decouple import config

client = OpenAI(api_key=config("OPENAI_KEY")) #need_key

def get_openai_response(messages):
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return chat_completion.choices[0].message.content

def chatbot(user_input, messages):
    user_message = {"role": "user", "content": user_input}
    messages.append(user_message)

    response = get_openai_response(messages)

    mod_elevenlabs.text_to_speech(response)
    mod_typing_effect.typing_effect(response)
    print(mod_deepl.translate_text(response))
    
    assistant_message = {"role": "assistant", "content": response}
    messages.append(assistant_message)  # Convert the text response to speech

    return response