#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#简单的格式化使用例子，穿插了input函数的使用
#注意input输入数字前要强制转换，他一般是指字符串
name=input("Please enter your name:")
score1=int(input("Please input your score last year:"))
score2=int(input("Please input your score this year:"))
if score1<score2:
    r1=((score2-score1)/score1)*100
    print('Congratulations!%s,you have improved %.2f%%.compared to last year'%(name,r1))
else:
    r1=((score1-score2)/score1)*100
    print('It\'s a pity %s,you have decreased %.2f%%.compared to last year'%(name,r1))
