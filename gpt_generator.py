import requests
import openai
from requests.auth import HTTPBasicAuth

wpUrl = 'https://staging3.staging2.blockchainspost.com/wp-json/wp/v2/posts/'

class GptGenerator(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GptGenerator, cls).__new__(cls)
        return cls.instance

    def _change_post_data(self, wp_url, post_id, username, app_pass, data):
        url = f'{wp_url}/wp-json/wp/v2/posts/{post_id}'
        response = requests.post(url, auth=HTTPBasicAuth(username, app_pass), json=data)
        if response.status_code == 200:
            print("Post updated successfully")
        else:
            print("Failed to update post")
            print("Status Code:", response.status_code)
            print("Response:", response.text)
        return response.json()

    def _generate_content(self, prompt, content, api_key, model):
        openai.api_key = api_key
        text_for_gpt = prompt + content
        content_len = int(len(text_for_gpt) / 3)
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
            new_content = response.choices[0].message['content']
            return response.choices[0].message['content']
        except Exception as e:
            print(str(e))
            return ['Error', str(e)]

    def generate_text(self, prompt, content, api_key, model, wp_url, post_id, username, app_pass):
        # new_content = self._generate_with_gpt( prompt, content, api_key, model)
        response = self._generate_content(prompt, content, api_key, model)
        title_idx_start = response.index('<title>')
        title_idx_end = response.index('</title>')
        title = response[title_idx_start + len('<title>'): title_idx_end]

        content_idx_start = response.index('<content>')
        content_idx_end = response.index('</content>')
        content = response[content_idx_start + len('<content>'): content_idx_end]

        desc_idx_start = response.index('<desc>')
        desc_idx_end = response.index('</desc>')
        desc = response[desc_idx_start + len('<desc>'): desc_idx_end]

        data = {
            'title': title,
            'content': content,
            'meta': { '_yoast_wpseo_metadesc': desc }
        }

        return self._change_post_data(wp_url, post_id, username, app_pass, data)
