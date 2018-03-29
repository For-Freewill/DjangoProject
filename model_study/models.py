# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

############## 第8课：20180328 ###################

class Author(models.Model):
    name = models.CharField(u"作者",max_length=200)
    email = models.EmailField(u"邮箱",null=True,default=None)
# Create your models here.

class Number(models.Model):
    number = models.CharField(u"书号",max_length=200)


class Book(models.Model):
    headline = models.CharField(u"大标题",max_length=255)
    pub_date = models.DateTimeField(u"出版时间",auto_now=True)
    authors = models.ManyToManyField(Author,related_name="author_set")
    number = models.OneToOneField(Number,default=None,null=True)
    class Meta:
        db_table="book"
        managed=True
        ordering=["pub_date","-id"]
        verbose_name=u"书籍"
        verbose_name_plural = u"书籍柜"

class Reply(models.Model):
    book = models.ForeignKey(Book,db_constraint=True,to_field="id",on_delete=models.CASCADE)
    content = models.CharField(u"回复",max_length=255)


############# 第8课：练习题目 ##############
class ClassNumber(models.Model):
    number = models.IntegerField(u"班号",null=False,unique=True)

class Grade(models.Model):
    classname = models.CharField(u"班级名",max_length=255,unique=True)
    start_date = models.DateTimeField(u"创建时间",auto_now_add=True)
    edit_date = models.DateTimeField(u"修改时间",auto_now=True)
    number = models.OneToOneField(ClassNumber,to_field="number",default=None,null=True)

class Teacher(models.Model):
    name = models.CharField(u"名称",max_length=255)
    age =models.IntegerField(u"年龄")
    sex = models.CharField(u"性别", max_length=2, null=False)
    grade = models.ForeignKey(Grade,to_field="classname",db_constraint=True,on_delete=models.CASCADE)

class Student(models.Model):
    stu_name = models.CharField(u"班级名",max_length=255,null=False)
    age = models.IntegerField(u"年龄",null=False)
    sex = models.CharField(u"性别",max_length=2,null=False)
    grade = models.ForeignKey(Grade,to_field="classname",db_constraint=True,on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher,related_name="stu_teacher")


