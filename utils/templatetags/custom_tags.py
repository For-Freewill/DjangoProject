# -*- coding: utf-8 -*-

from django import template

import datetime

# register = template.Library() 代表该文件是一个自定义标签的包
# register 不能做任何修改，一旦修改，该包就无法引用
register = template.Library()


#自定义过滤器
# 在模版中使用方式如下： {{message|mycut:"h"}}
@register.filter
def mycut(val, args="123"):
    # val: 代表管道符左边的参数， 该值是必须的， 因为自定义过滤器必须使用在变量上，所以必须要有一个val
    # args： 可配置的，如果有其它的参数，就代表你需要输入一个值

    # 编写你需要处理的代码
    # 在python2中，如果你是需要处理中文，我们一般都会使用unicode编码，即在字符串中的首位添加u
    return u"这是一个自定义过滤器，它的处理结果为 ： %s" % (val.replace(args, "").lower())


# 自定义标签，可以没有参数
@register.simple_tag
def curr_date(args):
    return datetime.datetime.now().strftime(args)


# 自定义包含标签
@register.inclusion_tag("my_menu.html")
def my_menu():
    menu = ["新建", "修改"]
    return {"menu": menu}