#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2025/5/3 14:27
# @Author  : 李佩锡11
# 将json数据转换为expand()接收的格式类型，也就是将[{},{},{}]转换成[(),(),()]
def get_param_data():
    data=[
        {'body':{"mobile":"13800000002","password":"929itheima.CN032@.20250430"},
         'success':True,
         'status_code':200,
         'message':"登陆成功"},
        {'body':{"mobile":"13801231231","password":"929itheima.CN032@.20250430"},
         'success':False,
         'status_code':200,
         'message':"用户名或密码错误"},
        {'body':{"mobile":"13800000002","password":"929itheima.CN032@.20250430@@@"},
         'success':False,
         'status_code':200,
         'message':"用户名或密码错误"}
    ]

    param_data = []
    # 将[{},{},{}]转换成[(),(),()]
    for i in data:
        param_data.append(tuple(i.values()))
    return param_data

if __name__ == '__main__':
    print(get_param_data())