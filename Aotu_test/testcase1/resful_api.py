import unittest,requests,os,openpyxl
from common.handlerequests import SendRequest
from common.handleconfig import conf1
from common.handlepath import *
from common.readexcel import ReadExcel
from library.ddt import ddt,data
from common.handle_token import Token_cls
from common.handlelog import log
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
from common.connectdb import Db_Utils
case_file = os.path.join(DATADIR,'apicases_1.xlsx')

@ddt
class Resful(unittest.TestCase):
    excel = ReadExcel(case_file,'resful')
    cases = excel.read_data()
    request = SendRequest()
    token = Token_cls().token()

    @data(*cases)
    def test001_resful(self,case):
        # 第一步：准备接口请求数据
        url = conf1.get("env", "url") + case["url"]
        method = case['method']
        title = case['title']
        # eval这个内置函数的作用：执行一个字符串表达式、并且返回执行后的结果
        json = eval(case['json'])
        row = case['case_id'] + 1
        print(row)
        headers = {"Content-Type":"text/plain","ID-Token":self.token}
        expected = eval(case['expected'])  # 用来和实际结果进行对比==》断言
        # print(headers)

        # #第二步：发送接口请求
        res = self.request.send(method=method,api="resful",url=url,headers=headers,json=json)
        # res = requests.post(url=url, json=json, headers=headers, data=None)
        result = res.json()
        print(result)

        #第三步：接口的断言
        try:
            if title == 'N00':
                self.assertEqual(expected['data'], result['data'])
                self.assertEqual(expected['code'], result['code'])
            else:
                self.assertEqual(expected['code'], result['code'])
                self.assertEqual(expected['command'], result['command'])
                # self.db = Db_Utils().find_one('select * from db') #引用数据库的sql
                # self.assertEqual(result['data'],self.db[0])  #与数据库内容比对
        except Exception as e:
            self.excel.write_data(row=row, column=9, value='未通过')
            log.error('用例{}执行未通过'.format(case['title']))
            log.exception(e)
            raise e

        else:
            self.excel.write_data(row=row, column=9, value='通过')
            log.info('用例{}执行通过'.format(case['title']))
#
if __name__ == '__main__':
    unittest.main()






