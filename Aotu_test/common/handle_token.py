import requests
from common.handlerequests import SendRequest
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

class Token_cls():
    def __init__(self):
        self.auth = HTTPBasicAuth("101".encode('utf-8'), "123456")
        # self.auth = 'Basic MTAxOjEyMw=='
        # self. url = "http://10.38.2.12:30090/hjmos-authcenter/oauth/token"  #开发环境
        self.url = "http://10.34.93.21:30768/hjmos-authcenter/oauth/token"    #测试环境

        self.method = "post"
        self.params = {
                  "scope":"read",
                  "username":"yeziyuan",
                  "password":"123456",
                  "grantType":"password"}
    def token(self):
        # res = requests.post(url=url,params=params,auth=auth)
        c = SendRequest()
        res = c.send(method=self.method, url=self.url, params=self.params, auth=self.auth)
        result = res.json()['data']['accessToken']
        return result


    def flash(self):
        print("取消订阅")

if __name__ == '__main__':
    d = Token_cls()
    w = d.token()
    print(w)


