import requests

notionURL = "https://www.notion.so/api/v3/"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 "
                  "Safari/537.36"
}
baseCookie = {
    'token_v2': 'v02%3Auser_token_or_cookies'
                '%3A57oC2RoyUYBgm76sEWp18naln_jrNw8ewzWfrkfxT4hSNaFBIT7U2pkdQXbeHjMxTgwaQS0oZGTSgiYjgxTzX'
                '-AUTZF9fGKEorMn6YH5uvtc7TV46eGA-BNvVBy53EJ851sJ'}


class NotionService(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(NotionService, cls).__new__(cls)
        return cls.instance

    def _request_notion(self, url, data, token):
        cookie = {'token_v2': token} if token else baseCookie
        return requests.post(notionURL + url, cookies=cookie, json=data, headers=headers).json()

    def _find_user(self, email, token):
        return self._request_notion('findUser', {'email': email}, token)

    def _invite_user_by_id(self, user_id, block_id, space_id, token):
        res = self._request_notion('inviteGuestsToSpace', {
            "block": {
                'id': block_id or "ff9defed-1b31-4a3b-be4b-d8e46b67f822",
                'spaceId': space_id or "b7b621eb-88cc-454f-b7d9-76a5feaec0e2"
            },
            "permissionItems": [
                {
                    "type": "user_permission",
                    "role": "reader",
                    "user_id": user_id,
                }
            ]
        }, token)
        print(res)
        return res

    def _create_user(self, email, token):
        return self._request_notion('createEmailUser', {
            "email": email,
            "preferredLocaleOrigin": "inferred_from_inviter",
            "preferredLocale": "en-US"
        }, token)

    def _get_user_id(self, email, token):
        user = self._find_user(email, token)
        if not len(user):
            created_user = self._create_user(email, token)
            return created_user["userId"]
        else:
            return user["value"]["value"]["id"]

    def invite_user(self, email, block_id, space_id, token):
        user_id = self._get_user_id(email, token)
        return user_id if not len(self._invite_user_by_id(user_id, block_id, space_id, token)) else 'error'

    def _remove_user(self, user_id, space_id, token):
        return self._request_notion('removeUsersFromSpace', {
            "userIds": [
                user_id
            ],
            "spaceId": space_id or "b7b621eb-88cc-454f-b7d9-76a5feaec0e2",
            "removePagePermissions": True,
            "revokeUserTokens": False
        }, token)

    def remove_user(self, user_id, space_id, token):
        return self._remove_user(user_id, space_id, token)
