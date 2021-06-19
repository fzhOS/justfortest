#!/usr/bin/env python 
# coding:utf-8
temp=0.0
input1=input('please input your temperature\n')
if input[:3] in ['RMB','rmb']:
        temp=eval(input1[3:])/6.78
        print('USD'+str(temp))
if input[:3]in ['USD','usd']:
        temp=eval(input1[3:])*6.78
        print('RMB'+str(temp))
else:
    print('输出格式错误')

