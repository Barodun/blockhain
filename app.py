from gpt_generator import GptGenerator
from flask import Flask, request, jsonify
from flask_cors import CORS
from requests.auth import HTTPBasicAuth

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
    wp_url = request.json['wp_url']
    post_id = request.json['post_id']
    username = request.json.get('username')
    app_pass = request.json.get('app_pass')
    res = gpt_generator.generate_text(prompt, content, api_key, gpt_model, wp_url, post_id, username, app_pass)
    print(res)
    return res

@app.route('/', methods=['GET'])
def default():
    # prompt = 'Translate this text to English. There is the text:'
    # content = 'There is the simple text to translate'
    # api_key = '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'
    # gpt_model = 'gpt-3.5-turbo'
    # res = gpt_generator.generate_text(prompt, content, api_key, gpt_model)
    # print(res)
    # return res
    # data = {
    #     'title': 'New Post Title',
    #     'content': 'This is the updated content of the post.'
    # }
    # post_id = '565'
    # username = 'generator@pansevich.me'
    # password = 'J%*ymb9x48%cXTK6mBMzU7#t'
    # response = gpt_generator._change_post_data(post_id, data, username, password)
    # return response
    wp_url = 'https://staging3.staging2.blockchainspost.com'
    post_id = 570  # ID of the post to update
    username = 'generator'
    app_pass = 'hpqJ CoHf Vugg xSv7 MRyp ZD0L'
    # Data you want to update
    data = {
        'title': 'New Post Title',
        'content': 'Updated content here',
        'meta': { '_yoast_wpseo_metadesc': 'New Yoast meta desc' }
    }
    return gpt_generator._change_post_data(wp_url, post_id, username, app_pass, data)

if __name__ == '__main__':
    app.run()
