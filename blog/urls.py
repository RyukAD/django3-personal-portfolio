# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:07:14 2020

@author: dubey
"""

from django.contrib import admin
from django.urls import path, include
from . import views
app_name='blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail')
    
]