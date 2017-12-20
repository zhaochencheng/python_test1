# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 23:20
# @Author  : zhaochencheng
# @QQ      : 907779487
# @version : Python 3.5.2
# @File    : example.py
# @Software: PyCharm Community Edition
mon =[1,2,3,4,5,6,7,8,9,10,11,12]
mon_day = [31,28,31,30,31,30,31,31,30,31,30,31]
month = 2
total = 0
if month >=2:
    total =1
for i in mon:
    if month >= (i):
        total = mon_day[i-1]+total
print(total)
# for i in mon_day:
#     total = mon_day[i]+total
# print(total)
