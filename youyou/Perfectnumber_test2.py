# -*- coding: utf-8 -*-
# @Time    : 2017/12/17 21:03
# @Author  : zhaochencheng
# @Site    : 
# @File    : Perfectnumber_test2.py
# @Software: PyCharm Community Edition
'''
求完全数

'''
for a in range(1,10000):
    total = 0
    L = []
    for i in range(1,a+1):
        if a%i==0:
            # print(i)
            L.append(i)
    # print(L)
    for x in range(0,len(L)-1):
        total = L[x] + total
    if total == a:
        print("%d is PerfectNumber!"%a)
    else:
        # print("%d is not PerfectNumber!"%a)
        # print("Pass")
        pass
    # print(total)