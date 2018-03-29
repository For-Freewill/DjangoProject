# -*- coding:utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
import views

urlpatterns = [
    url(r'model_study/$', views.ModelStudy.as_view()),
    url(r'model_study_test/$', views.ModelStudyTest.as_view()),
]

# 当出现404时，所需要展示的页面
# django.views.defaults.page_not_found 是django自带的404错误页面
# 我们同样可以指定一个view函数，自定义一个页面
# 如果要开启这个效果，我们需要在settings中，把关闭
# handler404 = 'django.views.defaults.page_not_found'
handler404 = 'hello.views.page_404'
handler500 = 'hello.views.page_500'