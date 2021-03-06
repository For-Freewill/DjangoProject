# -*- coding: utf-8 -*-
"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app1 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^app1/', include("app1.urls", namespace="app1")),
    url(r'^model/', include("model_study.urls", namespace="model_url")),
]


# 自定义404返回页面
# django.views.defaults.page_not_found 是django自带的404错误页面
# 我们同样可以指定一个view函数，自定义一个页面
# 如果要开启这个效果，我们需要在settings中，DEBUG = False
# handler404 = 'django.views.defaults.page_not_found' #默认的404处理页面
handler404 = 'app1.views.page_404' #自定义的404页面
handler500 = 'app1.views.page_500'

