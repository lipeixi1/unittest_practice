#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2025/5/1 13:34
# @Author  : 李佩锡11
import unittest
import requests


class Testlogin(unittest.TestCase):
    def setUp(self) -> None:
        print("Test start:")

    def tearDown(self) -> None:
        print("Test end")
    # 登录成功
    def test_login_ok(self):
        print("登录成功接口测试")
        res = requests.post(url="http://ihrm-java.itheima.net/api/sys/login",
                            json={"mobile": "13800000002", "password": "929itheima.CN032@.20250501"},
                            )

        # 添加响应断言
        self.assertEqual(200,res.status_code)
        self.assertEqual(10000,res.json().get('code'))
        self.assertEqual(True, res.json().get('success'))
        self.assertIn("登录成功",res.json().get("message"))

    # 登陆失败（账号错误）
    def test_login_fail01(self):
        print("登录失败接口测试")
        res = requests.post(url="http://ihrm-java.itheima.net/api/sys/login",
                            json={"mobile": "13800000003", "password": "929itheima.CN032@.20250501"},
                            )

        # 添加响应断言
        self.assertEqual(200, res.status_code)
        self.assertEqual(20001, res.json().get('code'))
        self.assertEqual(False, res.json().get('success'))
        self.assertIn("用户名或密码错误", res.json().get("message"))

    # 登陆失败（密码错误）
    def test_login_fail02(self):
        print("登录失败2接口测试")
        res = requests.post(url="http://ihrm-java.itheima.net/api/sys/login",
                            json={"mobile": "13800000002", "password": "929itheima.CN032@.20250430"},
                            )

        # 添加响应断言
        self.assertEqual(200, res.status_code)
        self.assertEqual(20001, res.json().get('code'))
        self.assertEqual(False, res.json().get('success'))
        self.assertIn("用户名或密码错误", res.json().get("message"))

    def test_login_Tpshop(self):
        # 创建session请求
        session = requests.session()
        resp01 = session.get(url='http://localhost/index.php?m=Home&c=User&a=verify&r=0.282476177880858')

        resp = session.post(url="http://localhost/index.php?m=Home&c=User&a=do_login&t=0.49716849158828313",
                            data={
                                'username': '13135364611',
                                'password': '123456',
                                'verify_code': '8888'
                            },
                            )
        # 添加断言判断
        self.assertEqual('登陆成功',resp.json().get('msg'))