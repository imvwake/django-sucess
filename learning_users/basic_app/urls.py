from django.contrib import admin
from django.urls import re_path as url
from django.urls import include
from basic_app import views

app_name='basic_app'

urlpatterns=[
    url('register/',views.register,name='register'),
    url('user_login/',views.user_login,name='user_login'),
]
