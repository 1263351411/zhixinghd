"""
author:木木夕
date:2019-11-10 23:36
"""

from django.conf.urls import url
from .views import Publications

# url前缀 /surfacemanager/
urlpatterns = [
    url(r'^publications$', Publications.as_view()), #publications
    url(r'^demos$', Publications.as_view()), #publications
    # url(r'^test$',test)
]