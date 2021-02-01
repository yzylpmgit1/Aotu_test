#coding=utf-8

import unittest
from common.handlerequests import SendRequest
from common.handlelog import log
from common.readexcel import ReadExcel
from library.ddt import data,ddt
from common.handleconfig import conf1,conf
import os
from common.handlepath import *
import requests
from requests.auth import HTTPBasicAuth
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
case_file = os.path.join(DATADIR,"apicases_1.xlsx")

@ddt
class Test_Login(unittest.TestCase):
    excel = ReadExcel(case_file,"login")
    cases = excel.read_data()  #列表==》2个及以上的字典==》1个字典就是一条用例
    request = SendRequest()

    @data(*cases)
    def test001_login(self,case):
        #第一步：准备接口请求数据
        url = conf1.get("env","url") + case["url"]
        # print(url)
        method = case['method']
        # eval这个内置函数的作用：执行一个字符串表达式、并且返回执行后的结果
        params = eval(case['params'])
        # print(params)
        auth = HTTPBasicAuth("1000001".encode('utf-8'), "123456")
        expected = eval(case['expected'])  #用来和实际结果进行对比==》断言
        # print(expected)
        row = case['case_id'] + 1

        # #第二步：发送接口请求
        c = SendRequest()
        res = self.request.send(method,api="login",url=url,params=params,auth=auth)
        # res = self.request.send(method, api="login", url=url, params=params)
        result = res.json()
        print(result)

        # 第三步：接口的断言
        # try:
        #     self.assertEqual(expected['code'], result['code'])
        #     self.assertEqual(expected['message'], result['message'])
        # except Exception as e:
        #     self.excel.write_data(row=row, column=9, value='未通过')
        #     log.error('用例{}执行未通过'.format(case['title']))
        #     log.exception(e)
        #     raise e
        # else:
        #     self.excel.write_data(row=row, column=9, value='通过')
        #     log.info('用例{}执行通过'.format(case['title']))

if __name__ == '__main__':
    unittest.main()

