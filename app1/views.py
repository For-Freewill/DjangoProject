# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views import View
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Article, Reply
import datetime

# Create your views here.
#########第2课：2018-3-19 ##########
class HelloWorld(View):
    def get(self,request):
        message = u'第一个Django页面'
        return HttpResponse(message)

#########第4课：2018-3-21 ##########
class Hello(View):
    def get(self,request):
        message = "<B>普通URL配置</B>"
        return HttpResponse(message)

class HelloCommon(View):
    def get(self,request):
        message = "普通长路径的URL配置"
        return HttpResponse(message)

class HelloRegular(View):

    def get(self,request):
        message = "普通带正则的URL路径的URL配置"
        return HttpResponse(message)

class HelloSingleNonPara(View):

    def get(self,request,para1):
        print("单个非命名参数para1:"+para1)
        message = "单个非命名参数的URL（）"
        return HttpResponse(message)


class HelloMultipleNonPara(View):

    def get(self,request,para1,para2,para3):
        print("多个非命名参数para1:"+para1+para2+para3)
        message = "多个非命名参数的URL:^app1/([0-9]{4})/([0-9]{2})([0-9]{2})/$"
        return HttpResponse(message)


class HelloSinglePara(View):

    def get(self,request,para1):
        print("单个命名参数para1:"+para1)
        message = "单个命名参数的URL:^para/(?P<para1>[abcd]{3})/$）"
        return HttpResponse(message)

class HelloMultiplePara(View):

    def get(self,request,para1,para2):
        print("多个命名参数para1:"+para1+para2)
        message = u"多个命名参数的URL:^para/(?P<para1>[abcd]{3})/(?P<para2>para2)$'）"
        return HttpResponse(message)

class RedirectPage(View):
    def get(self,request,para1):
        if para1=="1":
            # reverse
            # 未带参数
            return redirect(reverse("login"))

            # 带非命名参数的跳转
            #return redirect(reverse("articles",args=("2018","01","03"))) #from django.core.urlresolvers import reverse

            # 命名参数的跳转
            #return redirect(reverse("top:namespache", kwargs={"para1": "abc","para2":"para2"}))
            #实际跳转：http://192.168.73.128:8000/hello/para/abc/para2

            #return redirect(reverse("app:namespache", kwargs={"para1": "abc", "para2": "para2"}))
            #实际跳转：http://192.168.73.128:8000/app/para2/abc/para2

            # 如果name是唯一的时候，你可以直接只使用name
            # 但是如果name在其它include中也存在相同name，为了区分，我们可以给inlude设置一个namespace
            # 我们通过命名空间名称+名称访问
            # 为了程序的健壮性，我们尽量使用命名空间+名称访问
            # 顶层其实有一个app名称，但是我们日常开发中，几乎不使用，该功能了解知道即可
        else:
            return HttpResponse("重定向失败")

class Error500(View):

    def get(self,request):
        raise Exception
        message = u""
        return HttpResponse(message)

def page_404(request):
    mess = '自定义的404页面'
    return HttpResponse(mess)

def page_500(request):
    #raise Exception
    mess = '自定义的500页面'
    return HttpResponse(mess)

#### 第5课  2018-3-23 ##########
class CommonRender(View):
    def get(self,request):
        message = "<B>普通URL配置</B>"
        return HttpResponse(message)

class RenderTemplate(View):
    def get(self,request):
        #render默认已经import：from django.shortcuts import render,
        #render函数最少需要2参数，第一个是request，第二个是模板HTML文件的路径
        #第二参数的HTML路径是相当于settings的template路径

        #return render(request,"render_html.html")
        #相对路
        return render(request, "render/render_html.html")

class GetTemplate(View):
    def get(self,request):
        template = get_template("get_template.html")
        #template是一个对象
        #get_template 调用模板，是render方法的底层实现，返回的是字符串，而不是渲染后的HTML
        print template.render(),type(template.render())

        return HttpResponse(template.render())

class RenderParam(View):
    #动态渲染传递参数
    def get(self,request):
        message = "后台的message变量的内容"
        date = time.time().__repr__()
        #传递一个参数给前端页面，配置一个字典参数传递，key为前端页面的参数，value是定义的变量
        #return render(request,"render_paraml.html",{"mess":message})

        #传递多个参数到前端，要使用context={“”“”“”}
        #return render(request, "render_paraml.html", context={"mess": message, "date": date})

        #如果需要传递的参数过多，甚至是全部的时候吗，一使用locals()函数，代表全部变量.
        print(locals())

        return render(request,"render_paraml.html",context=locals())

class TemplateTag(View):
    #模板标签的额使用
    def get(self,request):
        message = "TestMessgae"
        date = time.time()
        days = ["Mondya","Tuesday","Thursday","Friday"]

        days_job = {
            "Monday":1,
            "Tuesday":2,
            "Wedesday":3,
            "Thrusday":4,
            "Friday":5
        }

        for index,day in enumerate(days):
            print index,day

        for index in days:
            print index

        hello = "hello world"

        now = datetime.datetime.now()
        print now.strftime("%Y-%m-%d %H:%M:%S")
        for index,day in days_job.items():
            print index,day
        return render(request,"template_tag.html",locals())

class TemplateExtend(View):
    #模板继承
    def get(self,request):

        return render(request,"extend_template.html",locals())

class TemplateExtend2(View):
    #模板继承
    def get(self,request):

        return render(request,"extend_template1.html",locals())

#### 第6课  2018-3-26 ##########
class CustomFilter(View):
    #自定义过滤器
    def get(self,request):
        message = "HELLO WORLD"
        return render(request,"custom_filter.html",locals())

# 自定义包含标签
# 我们使用include标签时，如果引入的html代码中需要传入变量，
# 则需要在所以引入的view视图中获取变量，如果引入的html代码中的变量是一个公共变量，
# 则需要重复获取N次
# 使用自定义包含标签，可以在自定义文件中获取一次即可
class CustomInclude1(View):
    def get(self, request):
        menu = ["博彩", "多少"]
        return render(request, "custom_include.html", locals())

class CustomInclude2(View):
    def get(self, request):
        menu = ["博彩", "多少"]
        return render(request, "custom_include1.html", locals())

class CustomInclude3(View):
    def get(self, request):
        return render(request, "custom_include2.html")

class CustomInclude4(View):
    def get(self, request):
        return render(request, "custom_include3.html")


class ImportStatic(View):
    #导入静态文件
    def get(self,request):
        return render(request,"import_static.html",locals())

#### 第7课  2018-3-27 ##########
class ModelOper(View):
    def get(self, request):
        # 新增一个文章的数据
        #INSERT hello_article(title, content, reply) VALUES ("怎么样在django中新增一条数据",
        # "我们可以使用django的save方法持久化一条数据", "这边文章写得真好")
        article = Article()
        article.title = "怎么样在django中新增一条数据"
        article.content = "我们可以使用django的save方法持久化一条数据"
        article.reply = "这边文章写得真好"
        article.save()

        # 以下为新增数据简写的方式
        # Article(title="怎么样在django中新增一条数据第二种方式",
        #         content="我们可以使用django的save方法持久化一条数据").save()

        # 查询所有表数据
        # 等同于select * from hello_article;
        # 这里返回的是一个QuerySet，实际就是一个数组
        articles = Article.objects.all()
        print articles

        for article in articles:
            # print article.__dict__
            print "-------------"
            print article.title
            print article.content
            print article.reply
            print "-------------"


        # 查询单个数据
        # 等同于select * from hello_article where id=1;
        # 在django 的ORM查询中，数据库的主键可以用PK代替
        # 通过get方式返回的数据，它只会返回一个对象
        # 如果通过条件返回的数据有多条或者找不到，都会报错
        # article = Article.objects.get(pk=1)
        # article = Article.objects.get(id=1)

        # 批量删除
        # 等同于 DELETE FROM hello_article WHERE status=1
        # 批量删除，如果找不到数据，就不会删除
        # Article.objects.filter(status=1).delete()

        # 删除单个
        # DELETE FROM hello_article WHERE id=1
        # 如果数据不存在，则会报错
        # Article.objects.get(id=1).delete()

        # 批量修改
        # UPDATE hello_article SET status=3 WHERE status=2
        # Article.objects.filter(status=2).update(status=3)

        # 单个修改
        # 实际上save方法如果当前实例已经存在于数据库中，它就会当初一个update操作
        # Article.objects.filter(id=7).update(status=4)
        # article = Article.objects.get(pk=7)
        # article.status = 1
        # article.save()

        return render(request, "model_oper.html", locals())