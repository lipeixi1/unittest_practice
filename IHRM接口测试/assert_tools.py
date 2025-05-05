#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2025/5/3 13:33
# @Author  : 李佩锡11

# 断言判断函数
def assert_login(self,res,success,status_code,msg):
    print(res.json())
    self.assertEqual(success, res.json().get('success'))
    self.assertEqual(status_code,res.status_code)
    self.assertIn(msg,res.json().get('message'))