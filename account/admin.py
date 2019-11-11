# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import User
from django.shortcuts import render

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs

    list_display = ('id', 'name', 'email')
    list_filter = ('id', 'name', 'email')
    fk_fields = ('id','name','email')

admin.site.site_header = "知行后台管理"
admin.site.site_title = "知行管理"
admin.site.register(User,UserAdmin)