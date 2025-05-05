#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2025/5/4 21:19
# @Author  : 李佩锡11
#Suit对象运行测试和生成报告
import unittest
from tp_reg_test import Test_tpshop_register
from htmltestreport import HTMLTestReport

if __name__ == '__main__':
    # 实例化suit对象，添加测试方法，指定报告生成文件，然后run
    suit = unittest.TestSuite()
    suit.addTest(unittest.makeSuite(Test_tpshop_register))
    runner = HTMLTestReport('./tpshop注册接口测试.html')
    runner.run(suit)