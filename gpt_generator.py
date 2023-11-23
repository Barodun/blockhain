import requests
import openai

openai.api_key = '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'
api_key = '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'
gptURL = "https://api.openai.com/v1/chat/completions"
# headers = {
#     'Authorization': f'Bearer {api_key}',
#     'Content-Type': 'application/json'
# }

baseCookie = {
    'token_v2': 'intercom-device-id-dgkjq2bp=5cfdfca5-81c6-484a-b917-c58415ee81d2; __stripe_mid=f46141a7-7774-4ec9-8b94-5100204d9100817dc5; __Host-next-auth.csrf-token=8ae1ec8e7ac670c7aeae9db3d3e73789c28736a219ea21ccc010ef387e73314c%7C9fdd9fab363aee869ecc4a75f8845eb34989422990f3aea034d5533e4dcd50e1; cf_clearance=1vJIz32g_enD53nyAOhW1Witbrmnt56QMwzUWlgTSkk-1700738791-0-1-b3f74f3b.700aa7f9.e4f610db-0.2.1700738791; intercom-session-dgkjq2bp=RjBVMlJ1ZXBLRG0ya3lGSVd2RGwrKytubERRNWVnOXQ3RUtka2NsREZBVk00ZVFSM2FESHpYellZYTA5NjhSaS0tc05CdzJGeUloekZ6MEhFVEtxbjVpZz09--f0e87dc37ec7c3681337a51b9c80b5a03507f5ae; __cflb=0H28vVfF4aAyg2hkHEuhVVUPGkAFmYvkJyAXYYpL9bs; _uasid="Z0FBQUFBQmxYMGd4Rmo2M29IOVNlSzJOem1oZVpTaWstUGJzcEMwRWZqZkxiS3gtVGRjYjVXYlRLU3EtcnZOUXZibG4yTnVXMUhCN19IV0hPb0JLRFRjcW1HU1ppUGJkZUtyRXluWDYxckZ0QTRoZVM1bjM3NXUtenUtenhBQnZ5cG9Cbi1Qdkd1MFJXbXJFbU0wcjFTQ3g4TGN0XzYtWHg1dVM5djhUQXlkZEgwOThkdnJzWW5tdl9IYzNaLURKZGE3ZTdHOW5NMXdMSzJ3bmE2bnByNFJ4Slh2NjJ5SFpoN3dCOXBUeDhmbjFGQnFCOWdzZWdmby1ScTAxUHRHVmlMRDItZlloS3VYY2N2UWR0TzNfQi1La09uWU1YNzJiMUJxcGVUb2V5cjFQSUF0UkFuaDdRREpLUmdPXzM0OExHblRCQ1ZPVGdtVEtfYV9EdVFXNllscTNhWjVmdzlfODJBPT0="; _puid=user-aAVlDl5zaIhpICTYTqx6PENm:1700743319-Atq6ARms3EG0VVTtHk1J5dhGnqRRWIObFmFG4CZJgwY%3D; __cf_bm=LSvA8pCAzZpHED.0QL0t7TprSwj0f5gfFScQYrJCtqk-1700743354-0-Ab8S3XhtxvHLOWZvFqEV7CZHhrBVtgyH+HwAmWBpJ6lYpqQTDJ5AXDeFyqnvcxFhLkFlw7UUb2IsqK5k+K5UTig=; _cfuvid=hIh.ZtYWHSvz5FaXsYqwWzGzBLoypMJVVUXWr3znREc-1700743354177-0-604800000; cf_clearance=WT_.NfFk8pjCTmc.mjE2qfkUpT_91v5JxQKSDX5Q8N4-1700743559-0-1-934e88bc.df02c9bd.c44fd75c-0.2.1700743559; ajs_user_id=user-dhFrp3aRSbk7K498JfVTcuGL; __Secure-next-auth.callback-url=https%3A%2F%2Fonramp.g1.services.openai.com; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..ajPIduRqelIwm0P8.p58szpmcmpVftbVf48jiBRUEF0THIHzeqnLGHKt2E_E4xjTxeQHXN_49vg2MY1aTyWPOCqynELGTFGPeJ3u0icmP_TaFFbu9SVUMptlpTaTqdu7qCVsRmJ2ECM0sJo4AVj0qZsNXg1orhxL-0QOXkXTUHo8fPQOPgtOeDmBdbsy7j6AwR5YAZI7wunpiRtjsKQd2jzA2O3tb-XiWc0uqbOZtBDgnuqocBdX29ef3q9xJm_dZgiLewEpW19X4YRki94iqbZVRM95zJl81_0QA-PXna-JOOhpqDPzfoNnuYqSE2gOXPift94cYaoAcF5gBinJfqWfSpHy94D_6fm9R3zzzIPWvMXBMVaVI2EBLRTrBtYfmYtAK-pjkTqJnaGCDVeko_59EoJm-cgTbMb3JK63Q8k_WbrHxD0RgvKOa5_dC03f4sbt92JjVb5bjXczz43bP0mFJtS-NY568xoxpyV4UCpEtlgrISX7kWDntDq19mW1bJ-AxIhhayttPHvwQcNOmCybq6gpSkwkHahJbbDuDSxpN8kS1LSZnPNBhVyzsO0WQEWhfCcBkSmXRyWUeGdqreB07fIkRnrVKXad6CUdeGO6W036HiNwbiYm-Jd7uAjJ-uJZfjiqfwRtJ34y2CRlXYOIYcRGOdH8e15UMgKkOkgRTUGxHJkfCGcqc044KvTMVYQAOofS9qBzv80QTWe_AkziYh1YxG31EHkaDR-LMXpNEI0OH3XJmOfoGbTC8d4l5axN6uFy7VHGVN4IKy5cfZCHkAmB2u0V_YgbZDCGQp6qmDnERpVNGOXJ2jj-jPzo8xosQQ-MeNj72itSMMx27R-t62epaSqFLCXBE1GEI1e_k0urXIgIZUjrfr2P5CuLLE8asp48_GntQSjj5VfGCNZr1fMFXwE2ZaTLh5E1GV7o_lu2yinHKHYqlFpiK6pE-L9_LTC7jz7waWPbe7u_Get00PMVYxbydZZYYCEM3kPLP3m1DTegTdAtOQSl1bNQqpQCJMHh1ZG-AbWvbLVMtOm5RlFd_SpkDw-kYZLuHebwJqpO-9wE0IJldA0VdYcHv6pDgaVVqAzIxj-8G58Aj8MxHoKTzqoaB_jEjtdmZrZAFrA50k0Nv3cgWB0oC6TT8g2dgcWZd4CuCZj5u1UW2WhIemJyZ-9KwqtXkuMzm3hc5cpKqWc7JvPQKxDiB82bW0dYRRxAhrPXuxzYKdxYWwlS4saoQnMQ-T21pa-DTFwDikX4HyG9rDa2evEDiH1q6pxwI6D0O-27bkuaFiITuPlfU5ZcaaJZHvEbQOk0lTo3DLdYog2iRgIkn7P35H1c4JUD0y9OtLg38A6O6t5izqGgUNhxq61ttljXqcWjPvLHQD1gUVAKa4uLhoTopPpb0M5oDdsDEVXd-PCkPoUO8JtMfdNcTFHuDigQ-uiZ1_mHYFZEkp3ETajVX7Hsa-6qNHcCHfpRVB06SgtXEMJKftS3QPZ0a2EVyNyYwIch9gYAbCgat3FJBjveFXa4Gyg72zwMavZsaDKUOeddvLsg0uxMkb_XpTcBu9l6_hnD_NDpBt4gFFck08YkpB_ZO6BH6u_U7EJlYepNRHxTghsG46kncbti4RsxojNUyZYHnjGYfQzU8qyB8nB-mA1ftRtrDhKg64t2WjYQfsLnj6qyq6qM1xLgeFRoQDOLevNmT4lHDhwS1U44CZpHNV4ekQ4SKoCkscxfZO5XgoV1p-Bx6mh5cSF0tv0oSF9Kgk72y003oHvuulQHhxnHEcUnxaRJm4R6iqT5J5WWl49WxssgPhSXBwFJon_qUmwU0O8N_5VuxBeHlyBPu25-T76Enb0aXqi4TmJ8Il-83ZOsBATgQpQ4AVNeNGRujkqXLCkn-UZujJj9or8cPShz58p0j0aUmNImRbUOsRTbk8fWlvTxvy2SJTnlJY6PC7bNkQvWWRkZj1WMXECIKL4c2ydDoGCirUwOFaPrF-EAV6jbnw8rHXR5ZXnvnr14uIltkWOmie5AvV_K-BAKw7c2Rge9QIE-DXYwvSZoAG3FAUwyQz8jHgOXb6wohuiCpPm9dCz6nyMt2JYtngkemBmsBMImSmqA26BXE2GJ63--yVkMsqGsnO7rkCao7ET7-rOcj5qszkbImQ-ZTMqnKSzFx3VRKXp1_nKDp2NRmmYP_46paAqQPWt85ivPOmLLWYcFE6_Omjy-M-PRcmkV6ZY2nh_z4FW-A_i8T78mlgB8WVFBk06Ia5w1x1VqILbnS6Za6CMldHCcvWjuEae1Kq253uWQiamro1LCreYX56hVdjXCXCVyUSjYeAejsOhww1I68SFCpIblG4_HtUszEfzaSrJUEB4UPqiSvhzJ9R82yNVpZkJ5Dery5MlTjZiSLzzTD1UQSo2CUqhU-HZRCY861W8cW9d5vKao-bTyxQShrFUggTs33tpL_fx9APYhS47D6nZWo2uxQwJ2hVOe8ASUtm7t9fAHyBJtvM_r1PaVyZ-UHuU0pKhULnNcAoGMQZC4bVGJd3KYnAHWDrr9ppPkJC9--utf-kF0alwmPWqbK34YOEoaazUHtJGfXuwKNLFJ82z8iYSCBX9qGlY4hTj96UU4VsKRBF5YlHja7pTmGZhd8RhgIRJAduGIBKI_Q3RRr2RdtHkMXmSvmfKVTltnTgr1QUnwIGpTp8SqodlU-g5QfPqrQnljeYcDTAkTqNtpI71pVUVKcJ3D5kBI-rqx6uAH5fP9RyWyMeIBJIvM0D5B2TkAS1uUHnQ6JOpY2-v6AjkeEsuQiXWV4EceS1fHBus0WVBn-cxPestBytII9GUMjOitZ0psZk8-Z4K9rE2egPBQn_13NiV2QwzY6XZCnDqbg4gzGmVCzTpoppxhk5f0hHqDGLBMoSMscdIP3AI1JIqI.APRVKUg9hy6MuSyQCzPjAQ; __cf_bm=YlcbUTL6XyCva8xf2f6yFqkhCOGLk__nnZhl2yHL6Vg-1700743577-0-ATtKNol0uKcXDx0XzDLcBnM36xT7rOdsfVcAPJgo7jMDdFz3ndoWFozrbAFyflY5TXW3Oab2MWvhdIz14Asb4zQ=; _cfuvid=TJbtxzotRl4W2c2vy_22CibEPcktoHTCrgJl2xKyr2M-1700743577790-0-604800000'}


class GptGenerator(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GptGenerator, cls).__new__(cls)
        return cls.instance

    def chat_with_gpt(self, prompt, api_key, model="gpt-3.5-turbo"):
        openai.api_key = api_key

        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message['content']
        except Exception as e:
            return str(e)

    def get_completion(self, prompt, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
        frequency_penalty = 0.0,
        presence_penalty = 0.0,
        stop = ["<!--noindex-->"],
        n = 1,
        max_tokens = 10,
        )

        return response.choices[0].message["content"]

    def test_fun(self, promt):
        return promt

    # def requset_gpt(self, prompt):
    #     data = {
    #         'model': 'gpt-3.5-turbo',
    #         'messages': [
    #             {
    #                 'role': 'user',
    #                 'content': prompt,
    #             }
    #         ],
    #         'max_tokens': 1024,
    #         'n': 1,
    #         'stop': ["<!--noindex-->"],
    #         'temperature': 1,
    #         'frequency_penalty': 0.0,
    #         'presence_penalty': 0.0,
    #     }
    #     # cookie = {'token_v2': token} if token else baseCookie

    #     # Make the POST request
    #     response = requests.post(gptURL, cookies=baseCookie, json=data, headers=headers)

    #     # Check if the request was successful
    #     if response.status_code == 200:
    #         return response.json()
    #     else:
    #         return 'error' + response.text

    def _request_notion(self, url, data, token):
        cookie = {'token_v2': token} if token else baseCookie
        return requests.post(gptURL + url, cookies=cookie, json=data, headers=headers).json()

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
