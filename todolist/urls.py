# -*- coding: utf-8 -*-
# @Author: liaohch3
# @Date:   2020-02-02 00:12:48
# @Last Modified by:   liaohch3
# @Last Modified time: 2020-02-02 00:17:16

from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home)
]
