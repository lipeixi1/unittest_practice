#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2025/5/3 14:15
# @Author  : 李佩锡11
import unittest

from htmltestreport import HTMLTestReport

from IHRM_test import Test_login
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_login))
    runner = HTMLTestReport('./测试报告/IHRM系统登录模块接口测试报告.html')
    runner.run(suite)
