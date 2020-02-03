# -*- coding: utf-8 -*-
# @Author: liaohch3
# @Date:   2020-02-02 00:12:48
# @Last Modified by:   liaohch3
# @Last Modified time: 2020-02-03 12:07:13

from django.urls import path
from . import views 

app_name = 'todolist'
urlpatterns = [
    path('home/', views.home, name="主页"),
    path('about/', views.about, name="关于"),
    path('edit/<item_id>', views.edit, name="编辑"),
    path('delete/<item_id>', views.delete, name="删除"),
    path('finish/<item_id>', views.finish, name="划掉"),
    path('unfinish/<item_id>', views.unfinish, name="撤销"),
]
