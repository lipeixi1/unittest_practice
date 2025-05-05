#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2025/5/3 15:37
# @Author  : 李佩锡11
#测试方法封装
import unittest
from parameterized import parameterized
import tp_reg_api as api
from tp_reg_param import get_paramdata
from tp_reg_assert import tp_reg_assert

class Test_tpshop_register(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("测试开始")
    @classmethod
    def tearDownClass(cls) -> None:
        print("测试结束")

    @parameterized.expand(get_paramdata)
    def test_reg(self,body,status,status_code,msg):
        res = api.tpshop_req.get_res(body)
        # 调用断言方法进行断言判断  将slef，响应，后面的是参数化数据里面的预期结果
        tp_reg_assert(self,res,status,status_code,msg)

