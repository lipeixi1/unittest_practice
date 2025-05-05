#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2025/5/2 22:07
# @Author  : 李佩锡11
import requests

class tpshop_loginin_api():
    @classmethod
    def get_verfity(self,session):
        session.get(url='http://localhost/index.php?m=Home&c=User&a=verify&r=0.282476177880858')

    @classmethod
    def get_login_res(self,session,data):
        res = session.post(url="http://localhost/index.php?m=Home&c=User&a=do_login&t=0.49716849158828313",data=data)
        return res
