#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2025/5/3 13:09
# @Author  : 李佩锡11
import unittest
import requests
from IHRM接口测试 import request_api as rep
import assert_tools as at
from parameterized import parameterized
from IHRM_params import get_param_data
# 测试接口层
class Test_login(unittest.TestCase):

    @parameterized.expand(get_param_data)
    def test_login(self,body,success,status_code,message):
        res = rep.request_api().login_post(body)
        at.assert_login(self,res,success,status_code,message)

    # # 手机号未注册
    # def test_login_fail01(self):
    #     json_data = {"mobile": "138000000123", "password": "929itheima.CN032@.20250430"}
    #     res = rep.request_api().login_post(json_data)
    #     at.assert_login(self,res,False,200,"用户名或密码错误")
    #
    # # 密码错误
    # def test_login_fail02(self):
    #     json_data = {"mobile": "13800000002", "password": "929itheima.CN032@.20250411"}
    #     res = rep.request_api().login_post(json_data)
    #     at.assert_login(self,res,False,200,"用户名或密码错误")