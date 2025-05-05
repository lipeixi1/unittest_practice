#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2025/5/2 19:48
# @Author  : 李佩锡11
import pymysql

class CRUDtools(object):
    # 类全局属性定义
    conn =None
    @classmethod
    def __getcon(cls):
        if cls.conn == None:
            cls.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='tpshop2.0')
        return cls.conn

    @classmethod
    def __closecon(cls,cursor):
        cls.conn.close()
        cursor.close()

    # 实现查询的方法
    @classmethod
    def find_mysql(cls,sql):

        res = None
        cls.__getcon()
        cursor = cls.__getcon().cursor()

        try:
            cursor.execute(sql)
            res = cursor.fetchall()
        except Exception as err:
            print(f'error message is {err}')
        finally:
            cls.__closecon(cursor)
            print(res)

    # 增删改方法
    @classmethod
    def CRUD_mysql(cls,sql):

        res = None
        cls.__getcon()
        cursor = cls.__getcon().cursor()

        try:
            res = cursor.execute(sql)
            cls.conn.commit()
        except Exception as err:
            print(f'error message is {err}')
            cls.conn.rollback()
        finally:
            cls.__closecon(cursor)
            print(res)


if __name__ == '__main__':
    mysql01 = CRUDtools()
    # 插入
    # mysql01.CRUD_mysql("insert into tp_config(id,name,value,inc_type) values (110,'lipeixi','100','sms')")
    # 修改
    # mysql01.CRUD_mysql("update tp_config set name='lipeixi3号' where id=110")
    # 删除
    # mysql01.CRUD_mysql(sql='delete from tp_config where id=110')
    # 查询
    # mysql01.find_mysql(sql='select * from tp_brand')
