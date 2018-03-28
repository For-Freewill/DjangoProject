# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# 使用makemigrations 命令需要事项
# 1、一但将生成的migrations文件通过migrate命令同步至数据库以后，被操作的migrations文件不能再操作
# 2、如何避免上面的情况：
#     （1）不要对已经生成好的migrations文件做任何操作
#     （2）所有对数据库的操作同一个人做，并保留好一套migrations文件
#     （3）不要直接在数据库中修改任何操作，比如修改字段，添加字段，删除字段等等；

class Article(models.Model):
    # 如果没有添加主键，django会默认添加一个ID的主键
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    reply = models.CharField(max_length=50, null=False)
    # 如果是新增的字段
    # 要么设置它允许为空 例：null=True
    # 要么设置一个默认值，例：default=""
    # 这个是数据库的规则，因为如果是新增的字段，
    # 没有默认值或者不允许为空的话，数据库是不知道这个字段要怎么展示
    comment = models.CharField(max_length=50, null=True)
    status = models.IntegerField(default=1)


class Reply(models.Model):
    content = models.CharField(max_length=50)