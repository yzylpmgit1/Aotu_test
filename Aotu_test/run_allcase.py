#coding=utf-8
from library.HTMLTestRunnerNew import HTMLTestRunner
from common.handlepath import *
from common.handle_email import send_email
import time
import unittest
from common.handlelog import log
import flask, json
from flask import request,Flask, jsonify

# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)  #get请求执行
app = flask.Flask(__name__)     #post请求执行


'''生成测试报告'''
def auto_run():
    try:
        # 定义生成报告的名称
        now = time.strftime('%Y-%m-%d-%H-%M-%S')
        filename = REPORTDIR + "\\" + str(now) + '_api_report.html'
        discover = unittest.defaultTestLoader.discover(CASEDIR1,"test_*.py")
        f = open(filename,'wb')
        runner = HTMLTestRunner(stream=f,
                                title='resful接口自动化测试报告',
                                description='用例执行情况如下：',
                                tester='叶子源')
        runner.run(discover)

        f.close()
        # return {'报告路径': REPORTDIR, '报告名称': now + '_api_report.html'}
        return {'测试结果': '执行完毕了！！！', '报告名称': now + '_api_report.html'}
    except Exception as e:
        log.error("执行失败，错误原因为:{}".format(e))

if __name__ == '__main__':
    auto_run()
    send_email(filename,'resful接口自动化测试报告')











