# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from .models import Book,Author,ClassNumber,Grade,Teacher,Student
# Create your views here.
class ModelStudy(View):
    def get(self,request):
        # book = Book.objects.create(headline=u"大标题")
        # Author.objects.create(name="kevin2",email="Test@qq.com")
        # filter条件查询，它的各个参数是and的关系
        # select * from author where name="kevin", eamil="test@qq.com"

        # order_by 就是排序，不加减号，就是正序，加"-"就是逆序
        print Author.objects.filter(email="test@qq.com").order_by("-name")
        print Author.objects.filter(email="test@qq.com").order_by("-name").values()
        print Author.objects.filter(email__contains="test").values()
        print Author.objects.filter(email__contains="Test").values()
        print Author.objects.filter(email__icontains="Test").values()
        print Author.objects.filter(id__in=[1,3]).values()
        print Author.objects.filter(email__iendswith=".Com").values()
        import datetime

        # date1 = datetime.datetime(2015, 1, 1, 01, 01, 01)
        # date2 = datetime.datetime(2018, 3, 27, 01, 01, 01)
        # print Book.objects.filter(pub_date__range=(date1, date2))
        # Book.objects.
        print Author.objects.count()
        print Author.objects.exclude(email="test@qq.com").order_by("-name").count()
        print Author.objects.filter(email__isnull=True).values()
        print Author.objects.filter(name__contains="kevin")[1:3:2]
        print Author.objects.latest("name").name
        print Author.objects.earliest("name").name
        print Author.objects.last().email
        print Author.objects.exclude(name="kevin").values()
        return render(request,"model_study/model_study.html",locals())

class ModelStudyTest(View):
    def get(self,request):
        # # ClassNumber.objects.create(number=001)
        # # ClassNumber.objects.create(number=002)
        #
        # Grade.objects.create(classname=u"django框架班",number=2)
        # Grade.objects.create(classname=u"django框架班", number=1)
        # Teacher.objects.create(name=u"Kevin老师",age=28,sex=u"男",grade=u"django框架班")
        # Teacher.objects.create(name=u"山泉老师", age=28, sex=u"男", grade=u"django框架班")
        # Teacher.objects.create(name=u"不懂老师", age=28, sex=u"男", grade=u"django框架班")
        #
        #
        #
        # Student.objects.create(stu_name=u"学生1",age=20,sex=u"男",grade=001,teacher="['kevin老师','山泉老师']")
        # Student.objects.create(stu_name=u"学生2", age=21, sex=u"女", grade=002, teacher="['kevin老师','不动']")
        # Student.objects.create(stu_name=u"学生3", age=22, sex=u"男", grade=001, teacher="['山泉老师','不动老师']")
        #手动构造数据
        nan =Student.objects.filter(sex="男").values()
        big = Student.objects.filter(age__gt=20).values()
        all = Student.objects.all().order_by("age")
        allnan=Student.objects.exclude(sex="女").values()
        alls =Student.objects.count()
        lastgrade =Grade.objects.last().classname

        return render(request,"model_study/model_study_test.html",locals())