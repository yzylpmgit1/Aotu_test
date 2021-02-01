#coding=utf-8

import requests
from common.handlelog import log

class SendRequest(object):
    """
    编写请求方法
    """
    def send(self, method,url,params=None, data=None, headers=None, auth=None,json=None,cookie=None,timeout=None):
        try:

            if method == "get":
                if params != "":
                    response = requests.get(url=url, params=params, headers=headers)
                else:
                    response = requests.get(url=url,headers=headers)

            elif method == "post":
                response = requests.post(url=url,params=params,headers=headers,auth=auth)

            elif method == "delete":
                response = requests.delete(url=url,params=params,headers=headers,auth=auth)

            return response

        except Exception as e:
            log.error('您选择的方法有误,错误的原因为:{}'.format(e))













