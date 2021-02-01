#coding=utf-8

import logging
from common.handleconfig import conf
from common.handlepath import *

class HandleLog(object):

    @staticmethod
    def create_logger():
        """创建日志的收集器、设置日志等级"""
        mylog = logging.getLogger(conf.get("log","name"))
        mylog.setLevel(conf.get("log","level"))

        """创建输出到控制台的日志等级"""
        sh = logging.StreamHandler()
        sh.setLevel(conf.get("log","sh_level"))
        mylog.addHandler(sh)

        """创建输出到文件的日志等级"""
        fh = logging.FileHandler(os.path.join(LOGDIR,"log.log"),encoding='utf-8')
        fh.setLevel(conf.get("log","fh_level"))
        mylog.addHandler(fh)

        """定义输出日志的格式"""
        formater = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s:%(message)s'
        fm = logging.Formatter(formater)
        sh.setFormatter(fm)
        fh.setFormatter(fm)

        return mylog

log = HandleLog().create_logger()












