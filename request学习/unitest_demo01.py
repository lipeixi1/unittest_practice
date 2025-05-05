#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2025/4/30 17:46
# @Author  : 李佩锡11
import unittest
import requests

# ihrm登录
def logintest():
    res = requests.post(url="http://ihrm-java.itheima.net/api/sys/login",
                        json={"mobile": "13800000002", "password": "929itheima.CN032@.20250501"},
                        headers={"Content-Type": 'application/json;charset=UTF-8'}
                        )
    return res.status_code

#封装测试类,从unittest.TestCase继承
class Test001(unittest.TestCase):
    # 下面每一条相当于一个case用例
    def setUp(self) -> None:
        print("————————test start——————————")

    def tearDown(self) -> None:
        print("————————test ended——————————")

    def test_login01(self):
        res = logintest()
        self.assertEqual(200,res)# 断言响应结果

    def test_login02(self):
        pass