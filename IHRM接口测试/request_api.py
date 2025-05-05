#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2025/5/3 13:11
# @Author  : 李佩锡11
import requests

# 接口对象层
class request_api(object):
    @classmethod
    def login_post(cls,json):
           res = requests.post(url='http://ihrm-java.itheima.net/api/sys/login',json=json)
           return res