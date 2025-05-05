#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2025/5/2 22:25
# @Author  : 李佩锡11
import  unittest
import requests
from TPshop接口封装 import login_api as api

# 封装断言
def assert_common(self,res,status_code,msg):
    self.assertEqual(msg, res.json().get('msg'))
    self.assertEqual(status_code,res.status_code)


class Test_login(unittest.TestCase):
    # 所有请求之前申请一个session
    session = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.Session()

    # 每个测试执行之前获取验证码
    def setUp(self) -> None:
        api.tpshop_loginin_api.get_verfity(self.session)

    def test_ok(self):
        res = api.tpshop_loginin_api.get_login_res(self.session,data={
                           'username':'13135364611',
                           'password':'123456',
                           'verify_code':'8888'
                       })
        assert_common(self,res,200,"登陆成功")

    def test_fial1(self):
        res = api.tpshop_loginin_api.get_login_res(self.session,data={
                           'username':'13135364611asd',
                           'password':'123456',
                           'verify_code':'8888'
                       })
        assert_common(self,res,200,'账号不存在!')


    def test_fial2(self):
        res = api.tpshop_loginin_api.get_login_res(self.session,data={
                           'username':'13135364611',
                           'password':'123456asd',
                           'verify_code':'8888'
                       })
        assert_common(self,res,200,'密码错误!')


if __name__ == '__main__':
    Test_login()