#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2025/5/1 20:22
# @Author  : 李佩锡11
from PyMysql.Sql封装 import CRUDtools

def Pymysql_test():
    import pymysql
    con = None
    cursor = None
    try:
        # 建立连接
        con = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="123456",database='tpshop2.0')
        # 创建游标
        cursor = con.cursor()
        # 使用游标对象执行sql语句
        cursor.execute('select * from tp_goods')
        #查询需要提取结果，增删改需要进行事务的提交或者回滚
        res = cursor.fetchone()
        print(f'查询结果为:res = {res}')
        # 关闭数据库和游标
        cursor.close()
        con.close()

    except Exception as err:
        print(f'插入失败\n {str(err)}')
        print(Exception)

    finally:
        print("执行结束")
        con.close()
        cursor.close()

if __name__ == '__main__':
    Pymysql_test()