from common.readexcel import ReadExcel
import os
from common.handlepath import *
from openpyxl import Workbook
# 批量创建excel，路径和文件名自己定义
def creat_xlsx(num):
    N=1
    while N<= num:
        columns = []
        datas = []
        with open("./pvuv.txt") as fin:
            is_first_line = True
            for line in fin:
                line = line[:-1]
                if is_first_line:
                    is_first_line = False
                    columns = line.split("\t")
                    continue

                datas.append(line.split("\t"))

        workbook = Workbook()
        # 默认sheet
        sheet = workbook.active
        sheet.title = "默认sheet"
        # sheet = workbook.create_sheet(title="新sheet")
        sheet.append(columns)
        for data in datas:
            sheet.append(data)
        workbook.save(TESTDIR + "\\" '{}.xlsx'.format(N))
        N+=1

# 获取生成的xlsx文件名称，
def file():
    list1=[]
    path = os.path.join(TESTDIR)
    for path,dirs,files in os.walk(path):
        for i in files:
            if i.split(".")[1] == "xlsx":
                list1.append(i)
    return list1

# 插入数据,数据自己定义
def insert():
    for j in file():
        case_file = os.path.join(TESTDIR,j)
        excel = ReadExcel(case_file,"默认sheet")
        data = [i for i in range(50)]
        excel.write_data(1,1,str(data))


