#coding=utf-8

import openpyxl
from common.handlepath import *
case_file = os.path.join(DATADIR,"apicases_1.xlsx")

class ReadExcel(object):

    def __init__(self,filename,sheetname):
        self.filename = filename
        self.sheet_name = sheetname

    def open(self):
        '''
        封装一个打开Excel表格的方法
        :return:
        '''
        self.wb = openpyxl.load_workbook(self.filename)
        self.sh = self.wb[self.sheet_name]

    def read_data(self):
        """
        封装一个读取excel的方法
        :return:
        """

        # 调用方法open
        self.open()

        # 取到每一行的数据放入到元组datas当中
        datas = list(self.sh.rows)

        # 拿到表头的数据、表中第一行的数据作为键
        title = [i.value for i in datas[0]]  # print(title)  #['case_id', 'interface', 'title', 'method', 'url', 'data', 'expected', 'result']

        # 定义一个空的列表用来接收所有的接口用例
        cases=[]

        # 取除了第一行以外的所有的数据
        for i in datas[1:]:
            values = [c.value for c in i]
            print(values)

            # 把title表头变为键、把values变为值、然后通过zip函数进行配对、打包放入字典当中
            case = dict(zip(title,values))
            cases.append(case)
        return cases

    def write_data(self,row,column,value=None):
        '''封装一个数据回写的方法'''
        self.open()

        #把用例运行后的结果写入到Excel表格
        self.sh.cell(row,column,value)

        #保存Excel
        self.wb.save(self.filename)
        self.wb.close()


if __name__ == '__main__':
    r = ReadExcel(case_file,"车辆监控中心")
    print(r.read_data())
    # r.write_data(2,8,'通过')












