#!/usr/bin/env python 
# coding:utf-8
var = 0.01
result=1.0
for i in range(1,366):

    if i % 7 in [0,6]:
        result*=pow(1-var,1)
    else:
        result*=pow(1+var,1)

print('你的成长为{:.2f}倍!'.format(result))