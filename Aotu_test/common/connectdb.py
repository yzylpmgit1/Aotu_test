#coding=utf-8
'''

host=None, 
user=None, 
password="",
database=None, 
port=0

'''
import pymysql
from common.handleconfig import conf

import cx_Oracle
class Db_Utils(object):

    def __init__(self):


        '''拿到了数据库的连接对象'''
        self.conn = pymysql.connect(host=conf.get("db","host"),
                                    user=conf.get("db","user"),
                                    password=conf.get("db","password"),
                                    database=conf.get("db","database"),
                                    port=int(conf.get("db","port"))
                                    )
        #获取mysql数据库的游标对象
        #1.执行SQL语句
        #2.并返回结果
        self.cur = self.conn.cursor()

    def find_one(self,sql):
        '''封装查询一行数据的方法'''
        self.conn.commit()  #提交
        self.cur.execute(sql)
        return self.cur.fetchone()

    def find_all(self,sql):
        '''封装查询数据库的所有数据的方法'''
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def close(self):
        '''关闭数据库的连接'''
        self.cur.close()
        self.conn.close()


# if __name__ == "__main__":
#     restest = Db_Utils()
#     restest.find_one('select * from db')
#     print(type(restest.find_one('select * from db')))

print(Db_Utils.__name__)
print(dir(Db_Utils))









