#coding=utf-8

'''
在dos窗口pip3 install configparser
configparser ==》这个模块是专门用来处理ini文件的
'''

from configparser import ConfigParser
from common.handlepath import *


class HandleConfig(ConfigParser):

    def __init__(self,filename):
        ConfigParser.__init__(self, defaults=None)  # 重写optionxform的方法，让option输出区分大小写
        super().__init__()
        self.filename = filename
        self.read(filename)
        # super().__init__()    #继承父类的构造函数
        # self.filename = filename
        # self.read(filename)

    def write_data(self,section, option, value=None):
        '''往ini文件中写入内容'''
        self.set(section, option, value)
        self.write(fp=open(self.filename))

conf = HandleConfig(os.path.join(CONFDIR,"config.ini"))
conf1 = HandleConfig(os.path.join(CONFDIR,"config.ini"))
# print(conf.get("log","name"))   #结果：Pci



















