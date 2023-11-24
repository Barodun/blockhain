import requests
import openai

gptURL = "https://api.openai.com/v1/chat/completions"

class GptGenerator(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GptGenerator, cls).__new__(cls)
        return cls.instance

    def chat_with_gpt(self, prompt, content, api_key, model):
        openai.api_key = api_key
        text_for_gpt = prompt + content
        content_len = int(len(content) / 3)
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    # {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": text_for_gpt}
                ],
                temperature=0,
                max_tokens=content_len,
                top_p=1,
                frequency_penalty=0.01,
                presence_penalty=0.01,
                stop=["<!--noindex-->"]
            )
            return response.choices[0].message['content']
        except Exception as e:
            return str(e)

    def generate_text(self, prompt, content, api_key, model):
        openai.api_key = api_key
        text_for_gpt = prompt + content
        content_len = int(len(content) / 3)
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    # {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": text_for_gpt}
                ],
                temperature=0,
                max_tokens=content_len,
                top_p=1,
                frequency_penalty=0.01,
                presence_penalty=0.01,
                stop=["<!--noindex-->"]
            )
            return response.choices[0].message['content']
        except Exception as e:
            return str(e)