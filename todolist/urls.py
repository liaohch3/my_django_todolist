# -*- coding: utf-8 -*-
# @Author: liaohch3
# @Date:   2020-02-02 00:12:48
# @Last Modified by:   10151
# @Last Modified time: 2020-02-02 12:34:19

from django.urls import path
from . import views 

app_name = 'todolist'
urlpatterns = [
    path('home/', views.home, name="主页"),
    path('about/', views.about, name="关于"),
    path('edit/', views.edit, name="编辑"),
]
