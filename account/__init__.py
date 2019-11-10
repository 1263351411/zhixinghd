from django.apps import AppConfig
import os

default_app_config = 'account.accountConfig'

class accountConfig(AppConfig):
    name = os.path.split(os.path.dirname(__file__))[-1]
    verbose_name = "用户管理"