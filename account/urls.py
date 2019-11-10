#_*_coding:utf-8_*_

"""
author:木木夕
date:2019-11-09 21:26
"""

from django.conf.urls import url
from .views import Account_Login,Account_Reg

# url前缀 /account/
urlpatterns = [
    url(r'^$', Account_Reg.as_view()), #注册
    url(r'^login$', Account_Login.as_view()), #登录
]