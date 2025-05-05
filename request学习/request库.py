#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2025/4/30 15:38
# @Author  : 李佩锡11
import requests
import pymysql


# tpshop登录接口请求
def qingqiu_lianxi():
    res = requests.get(url="http://localhost/index.php?m=Home&c=User&a=do_login&t=0.49716849158828313",
                       data={
                           'username':'13135364611',
                           'password':'123123',
                           'verify_code':'8888'
                       },
                       headers={
                           "Content-Type":'application/x-www-form-urlencoded; charset=UTF-8'
                       }
                       )
    print(res.text)
    print(res.json())

# IHRM登录
def qingqiu_lianxi2():
    res = requests.post(url="http://ihrm-java.itheima.net/api/sys/login",
                       json={"mobile":"13800000002","password":"929itheima.CN032@.20250430"},
                       headers={"Content-Type":'application/json;charset=UTF-8'}
                       )
    print(res.text)
    print(res.json())

# tpshop删除属性(cookie+session认证)
def qingqiu_lianxi3():
    res = requests.post(url="http://localhost/index.php/admin/goods/delGoodsAttribute",
                        data={"ids":"330"},
                        headers={'Cookie':'Pycharm-3e942ef5=c79e4a29-847c-4036-b81f-cdbac60ae136; is_mobile=0; is_distribut=1; PHPSESSID=jlqs4b2sc9bbvled1m3uuu68i2; user_id=2593; uname=13135364611; cn=0; province_id=1; city_id=2; district_id=3; admin_type=1; workspaceParam=goodsAttributeList%7CGoods'}
                       )
    print(res.text)
    print(res.json())


def session_test():
    session = requests.session()
    # 使用session实例发起请求,自动存储和管理cookie
    resp_v = session.get("http://localhost/index.php?m=Home&c=User&a=verify&r=0.2559572401865077")

    # 使用session实例进行登录
    resp = session.post(url="http://localhost/index.php?m=Home&c=User&a=do_login&t=0.49716849158828313",
                       data={
                           'username':'13135364611',
                           'password':'123456',
                           'verify_code':'8888'
                       },
                      )
    # 使用session实例获取,此时cookie是存放在session实例中,所以无须指定
    resp_list = session.get('http://localhost/index.php/Home/Order/order_list.html')

    # print(resp.json())
    print(resp_list.headers)

# 使用session进行tpshop注册
def session_tpregister():

    session = requests.session()

    resp_v = session.get("http://localhost/index.php?m=Home&c=User&a=verify&type=user_reg")

    rep = session.post(url="http://localhost/index.php/Home/User/reg.html",
                 data={
                     'username': '13974235017',
                     'verify_code': '8888',
                     'password': '123123',
                     'password2':'123123',
                     'invite':'13135364611'
                 },
                 )

    print(rep.json())


if __name__ == '__main__':
    session_tpregister()
