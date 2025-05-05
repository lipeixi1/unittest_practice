#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2025/4/30 20:46
# @Author  : 李佩锡11
import time

# 装饰器,接受一个函数名进行装饰(添加功能)
def decorator(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(start_time-end_time)
        return result
    return  wrapper

# 被装饰函数

# 使用语法糖对square进行装饰
@decorator
def square(x):
    return x*x


if __name__ == '__main__':
    # 新建一个函数将装饰后的square进行接受
    decoraror_square = decorator(square)
    # 装饰以后的函数实现了记录运行时间的功能,这个功能是装饰器wrappper为添加的
    # print(decoraror_square(2))


    print(square(4),square.__name__)