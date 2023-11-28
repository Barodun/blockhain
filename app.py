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
    # wp_url = 'https://staging3.staging2.blockchainspost.com'
    # post_id = 570  # ID of the post to update
    # username = 'generator'
    # app_pass = 'hpqJ CoHf Vugg xSv7 MRyp ZD0L'
    # # Data you want to update
    # data = {
    #     'title': 'New Post Title',
    #     'content': 'Updated content here',
    #     'meta': { '_yoast_wpseo_metadesc': 'New Yoast meta desc' }
    # }
    # return gpt_generator._change_post_data(wp_url, post_id, username, app_pass, data)
    # return gpt_generator.generate_text()
    response = '1. <title>Bitcoin price increased by more than $2k in the past 24 hours</title>2. <content><p><img title="Bitcoin price increased by more than $2k in the past 24 hours" src="/wp-content/uploads/2023/11/ef15dfdfb2283ed490cf19d59ac53d6b.jpg" alt="Bitcoin price increased by more than $2k in the past 24 hours" /></p> <p>The entire top ten largest cryptocurrencies demonstrated positive dynamics over the past 24 hours</p> <p dir="ltr">The price of Bitcoin (BTC) increased by more than 5% from November 15th to 16th, reaching $37,890 against Tether USD (USDT) on the Binance exchange. As of 10:00 Moscow time, BTC is trading at $37,570.</p> <h2>BTC/USD</h2> <p>37,538 +1,879 (5.27%) Nov 16 10:39:14 1d 3d 1m 3m 1y 5y</p> <p dir="ltr">Price fluctuations in cryptocurrencies have led to a mass liquidation of traders margin positions on cryptocurrency exchanges. According to Coinglass, over the past 24 hours, more than 51,000 traders collectively lost over $155 million, with the largest liquidation amounting to $2.93 million on the Binance exchange.</p> <p dir="ltr">If the quotes go in the opposite direction to what the trader expected in margin trading, they start incurring losses. Losses reduce the margin size, and when it decreases to a critical value, the trader receives a notification from the broker to replenish the account. This notification is called a Margin Call. If the account is not replenished and the losses continue to grow, the broker will automatically close the positions opened by the trader.</p></content>3. <desc>Bitcoin price increased by more than $2k in the past 24 hours. The top ten largest cryptocurrencies demonstrated positive dynamics. BTC/USD: 37,538 +1,879 (5.27%). Price fluctuations led to a mass liquidation of traders margin positions, resulting in over $155 million in losses. Margin Call is issued when losses exceed the critical value.</desc>'
    title_idx_start = response.index('<title>')
    title_idx_end = response.index('</title>')
    title = response[title_idx_start + len('<title>'): title_idx_end]

    content_idx_start = response.index('<content>')
    content_idx_end = response.index('</content>')
    content = response[content_idx_start + len('<content>'): content_idx_end]

    desc_idx_start = response.index('<desc>')
    desc_idx_end = response.index('</desc>')
    desc = response[desc_idx_start + len('<desc>'): desc_idx_end]

    
    return desc


if __name__ == '__main__':
    app.run()
