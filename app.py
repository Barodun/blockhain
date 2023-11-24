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
    prompt = request.json['prompt']
    content = request.json['content']
    api_key = request.json.get('api_key')
    gpt_model = request.json.get('gpt_model')
    res = gpt_generator.generate_text(prompt, content, api_key, gpt_model)
    print(res)
    return res

@app.route('/', methods=['GET'])
def default():
    prompt = 'Translate this text to English. There is the text:'
    content = 'There is the simple text to translate'
    api_key = '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'
    gpt_model = 'gpt-3.5-turbo'
    res = gpt_generator.generate_text(prompt, content, api_key, gpt_model)
    print(res)
    return res

if __name__ == '__main__':
    app.run()
