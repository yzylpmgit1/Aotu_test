#coding=utf-8

import unittest
from common.handlerequests import SendRequest
from common.handlelog import log
from common.readexcel import ReadExcel
from library.ddt import data,ddt
from common.handleconfig import conf1,conf
import os
from common.handlepath import *
from common.handle_token import Token_cls
from requests.auth import HTTPBasicAuth

@ddt
class Test_Login(unittest.TestCase):
    """
    编写车辆监控中心的用例
    :param case:
    :return:
    """

    excel = ReadExcel(case_file,"车辆监控中心")
    cases = excel.read_data()  #列表==》2个及以上的字典==》1个字典就是一条用例
    request = SendRequest()
    token = Token_cls().token()
    auth = HTTPBasicAuth("101".encode('utf-8'), "123456")

    @data(*cases)
    def test001_login(self,case):
        """
        第一步：准备接口请求数据
        :param case:
        :return:
        """

        url = conf1.get("env","url_vehicle") + case["url"]
        method = case['method']

        # eval这个内置函数的作用：执行一个字符串表达式、并且返回执行后的结果,eval函数的参数必须为字符串，否则将报错
        params = eval(case['params'])
        headers = {"ID-Token":self.token}
        # expected = eval(case['expected'])  # 用来和实际结果进行对比==》断言
        # classification = case['classification'] # 用来和实际结果进行对比==》断言
        # row = case['case_id'] + 1    # 回写函数结果需要用到该行数

        """发起接口请求"""
        res = self.request.send(method,url=url,params=params,headers=headers,auth=self.auth)
        result = res.json()
        print(result)

        # self.excel.write_data(row=row, column=10, value=str(result))   # 可回写返回的结果至对应excel表，主要做数据对比


        """第三步：接口的断言"""

        # try:
        #     if classification == "正常系":
        #         self.assertEqual(expected['code'], result['code'])
        #         self.assertEqual(expected['data'], result['data'])
        #     else:
        #         self.assertEqual(expected['code'], result['code'])
        #         self.assertEqual(expected['message'], result['message'])
        #
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

