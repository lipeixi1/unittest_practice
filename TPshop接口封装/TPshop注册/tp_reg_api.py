#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2025/5/3 15:37
# @Author  : 李佩锡11
# tpshop注册请求函数封装
import requests

class tpshop_req(object):
    @classmethod
    def get_res(self,data):
        # 获取session对象
        session = requests.Session()
        session.get(url='http://localhost/index.php?m=Home&c=User&a=verify&type=user_reg&r=0.5887277084599697')
        res = session.post(url='http://localhost/index.php/Home/User/reg.html',data=data)
        return res


