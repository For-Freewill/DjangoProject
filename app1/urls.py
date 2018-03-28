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
from django.conf.urls import url
from django.contrib import admin
from app1 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    ### 第2课：2018-3-19 ####
    url(r'^app1/$', views.HelloWorld.as_view(),name="login"),# '''注意URL的匹配是第一个满足的条件未知，一般要加$结束，否则2,3相同'''

    ### 第4课 2018-3-21  #####
    #1.普通路径URL配置，建议使用$结尾,因为匹配是从上倒下，匹配到的第一个路径就返回。
    url(r'^app1/common/$', views.HelloCommon.as_view()),

    #2.普通路径带正则URL配置。访问路径：/app1/re,/app1/regular
    url(r'^app1/[regular]{1,8}/$', views.HelloRegular.as_view()),

    #3.单个非命名参数（）配置,访问路径必须为:/app1/0123456789/
    url(r'^app1/(0123456789)/$', views.HelloSingleNonPara.as_view()),

    #3.单个非命名参数（）带正则配置,访问路径必须为：/app1/abcd*1-3/
    url(r'^app1/(abcd){1,3}/$', views.HelloSingleNonPara.as_view()),

    #4.多个非命名参数URL，访问路径：/app1/2018/0321/
    url(r'^app1/([0-9]{4})/([0-9]{2})([0-9]{2})/$', views.HelloMultipleNonPara.as_view(),name="articles"),

    #5.单个命名参数URL,访问路径：/para/abc/
    url(r'^para/(?P<para1>[abcd]{3})/$', views.HelloSinglePara.as_view()),

    #6.多个命名参数URL访问路径/para/abc/para2
    url(r'^para/(?P<para1>[abcd]{3})/(?P<para2>para2)$', views.HelloMultiplePara.as_view(),name="namespache"),

    #7.# 重定向处理,访问路径：/redirect/1时。跳转到新的路径，具体的路径查看views函数的处理
    url(r'^redirect/(?P<para1>[0-9]{1})$', views.RedirectPage.as_view()),

    #8.异常处理
    url(r'^error500/$', views.Error500.as_view()),  # 500error

    #######第5课 2018-3-23########
    url(r'render_html/$', views.RenderTemplate.as_view()),  # render（request,"html"）
    url(r'get_template/$', views.GetTemplate.as_view()),  # get_template（"html"）,render方法的底层实现。
    url(r'render_param/$', views.RenderParam.as_view()),  # render参数传递
    url(r'temp_tag/$', views.TemplateTag.as_view()),  # 模板常用的标签
    url(r'temp_extend/$', views.TemplateExtend.as_view()),  # 模板继承
    url(r'temp_extend2/$', views.TemplateExtend2.as_view()),  # 模板继承



    #######第6课 2018-3-26########
    url(r'custom_filter/$', views.CustomFilter.as_view()),# 自定义过滤器
    url(r"custom_include1/$", views.CustomInclude1.as_view()),
    url(r"custom_include2/$", views.CustomInclude2.as_view()),
    url(r"custom_include3/$", views.CustomInclude3.as_view()),
    url(r"custom_include4/$", views.CustomInclude4.as_view()),
    url(r"import_static/$", views.ImportStatic.as_view()),

    #######第7课 2018-3-27########
    url(r"model_oper/$", views.ModelOper.as_view()),
]


# 自定义404返回页面
# django.views.defaults.page_not_found 是django自带的404错误页面
# 我们同样可以指定一个view函数，自定义一个页面
# 如果要开启这个效果，我们需要在settings中，DEBUG = False
# handler404 = 'django.views.defaults.page_not_found' #默认的404处理页面
handler404 = 'app1.views.page_404' #自定义的404页面
handler500 = 'app1.views.page_500'

