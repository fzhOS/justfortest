#!/usr/bin/env python 
# coding:utf-8
def stu_register(name,age,*args):  #*args会把多传入的参数变为tuple ,
    print(name,age,args[0],*args,args)
stu_register('fzhOS',21,'money','mac','switch','games','music')
stu_register('fzh',21,'delicious food')