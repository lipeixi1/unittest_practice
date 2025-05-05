#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2025/5/3 15:37
# @Author  : 李佩锡11
#参数化数据获取的转化

def get_paramdata():
    data = [
            {'body':{'username':'13135364626',
                    'password':'123123',
                    'password2':'123123',
                    'verify_code':'8888',
                    'invite':'13875087800'},
             'status':1,
             'status_code':200,
             'msg':'注册成功'},

            {'body': {'username': '1313536a!@#sd',
                      'password': '123123',
                      'password2': '123123',
                      'verify_code': '8888',
                      'invite': '13875087800'},
             'status': -1,
             'status_code': 200,
             'msg': '请用手机号或邮箱注册'},
            {'body': {'username': None,
                      'password': '123123',
                      'password2': '123123',
                      'verify_code': '8888',
                      'invite': '13875087800'},
             'status': -1,
             'status_code': 200,
             'msg': '请用手机号或邮箱注册'},

            {'body': {'username': '13135364611',
                      'password': '123123',
                      'password2': '123123',
                      'verify_code': '8888',
                      'invite': '13875087800'},
             'status': -1,
             'status_code': 200,
             'msg': '账号已存在'},

            {'body': {'username': '13135364699',
                      'password': '123123',
                      'password2': '123123123123',
                      'verify_code': '8888',
                      'invite': '13875087800'},
             'status': -1,
             'status_code': 200,
             'msg': '两次输入密码不一致'},

            {'body': {'username': '13135364699',
                      'password': '123123',
                      'password2': '123123123123',
                      'verify_code': '8888',
                      'invite': '13875087800'},
             'status': -1,
             'status_code': 200,
             'msg': '两次输入密码不一致'}
        ]

    param_data = []
    for i in data:
        param_data.append(tuple(i.values()))
    return param_data
