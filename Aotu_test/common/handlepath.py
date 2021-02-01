#coding=utf-8

import os

"""定义项目的根路径"""
BASEDIR = os.path.dirname(os.path.dirname(__file__))

"""定义conf配置文件的路径"""
CONFDIR = os.path.join(BASEDIR,"conf")

"""定义data的路径"""
DATADIR = os.path.join(BASEDIR,"data")

"""定义excel_import的路径"""
TESTDIR = os.path.join(BASEDIR,"excel_import")

"""定义logs的路径"""
LOGDIR = os.path.join(BASEDIR,"logs")

"""定义static路径下report的路径"""
REPORTDIR = os.path.join(os.path.join(BASEDIR,'static'),'report')

"""定义testcase存放的路径"""
CASEDIR1 = os.path.join(BASEDIR,"testcase1")

"""定义data下的用例文件存放的路径"""
case_file = os.path.join(DATADIR,"apicases_1.xlsx")











