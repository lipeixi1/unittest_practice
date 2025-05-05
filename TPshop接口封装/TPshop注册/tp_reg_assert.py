#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2025/5/3 15:37
# @Author  : 李佩锡11
# 断言封装
def tp_reg_assert(self,res,status,status_code,msg):
    # 将接受的请求转换成json数据
    res_json = res.json()
    # 断言判断
    self.assertEqual(status,res_json.get('status'))
    self.assertEqual(status_code, res.status_code)
    self.assertEqual(msg, res_json.get("msg"))