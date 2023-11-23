from gpt_generator import GptGenerator
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
gpt_generator = GptGenerator()


# @app.route('/invite', methods=['POST'])
# def invite():
#     email = request.json['email']
#     token = request.json.get('token')
#     space_id = request.json.get('space_id')
#     block_id = request.json.get('block_id')
#     user_id = gpt_generator.invite_user(email, block_id, space_id, token)
#     return {'user_id': user_id}


@app.route('/generate', methods=['POST'])
def generate():
    user_id = request.json['user_id']
    space_id = request.json.get('space_id')
    token = request.json.get('token')
    res = gpt_generator.remove_user(user_id, space_id, token)
    print(res)
    return res

@app.route('/', methods=['GET'])
def default():
    return gpt_generator.chat_with_gpt('Generate simple text', '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')

# @app.route('/', methods=['GET'])
# def default():
#     # Your OpenAI API key
#     api_key = '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'

#     # Endpoint URL for OpenAI GPT
#     url = "https://api.openai.com/v1/chat/completions"

#     # Headers including the API key
#     headers = {
#         'Authorization': f'Bearer {api_key}',
#         'Content-Type': 'application/json'
#     }
#     prompt = "Translate the following English text to French: 'Hello, how are you?'"
#     # Data payload including your prompt
#     data = {
#         'prompt': prompt,
#         'max_tokens': 150  # Adjust the number of tokens as needed
#     }

#     # Make the POST request
#     response = requests.post(url, headers=headers, json=data)

#     # Check if the request was successful
#     if response.status_code == 200:
#         print(response.json())
#         return response.json()
#     else:
#         print(response.text)
#         return {'error': response.text}


if __name__ == '__main__':
    app.run()
