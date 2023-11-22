from notion_service import NotionService
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
notion_service = NotionService()

# asf


@app.route('/invite', methods=['POST'])
def invite():
    email = request.json['email']
    token = request.json.get('token')
    space_id = request.json.get('space_id')
    block_id = request.json.get('block_id')
    user_id = notion_service.invite_user(email, block_id, space_id, token)
    return {'user_id': user_id}


@app.route('/remove', methods=['POST'])
def remove():
    user_id = request.json['user_id']
    space_id = request.json.get('space_id')
    token = request.json.get('token')
    res = notion_service.remove_user(user_id, space_id, token)
    print(res)
    return res


if __name__ == '__main__':
    app.run()
