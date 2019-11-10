# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    class Meta:
        db_table = 'user'
        verbose_name = verbose_name_plural = "用户信息"
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=48, null=False,verbose_name="用户名")
    email = models.CharField(max_length=65, null=False, unique=True,verbose_name="邮箱")
    password = models.CharField(max_length=128, null=False,verbose_name="密码")

    def __repr__(self):
        return "<User {} {} {} {}>".format(
            self.id, self.name, self.email, self.password
        )

    __str__ = __repr__
