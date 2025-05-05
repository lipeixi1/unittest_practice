#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2025/4/30 21:25
# @Author  : 李佩锡11
import unittest
from htmltestreport import HTMLTestReport

from request学习 import unitest_login


def create_suite():
    # 创建suite实例
    suite = unittest.TestSuite()

    # 添加测试对象到suite
    suite.addTest(unittest.makeSuite(unitest_login.Testlogin))

    #创建htmltestreporter实例对象
    runner = HTMLTestReport("./测试报告/IHRM登录测试报告.html")

    # 将suite实例传入runner.run()
    runner.run(suite)

if __name__ == '__main__':
    create_suite()