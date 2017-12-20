# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 21:01
# @Author  : zhaochencheng
# @QQ      : 907779487
# @version :Python 3.5.2
# @File    : test_1.py
# @Software: PyCharm Community Edition
'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。

'''
sum = 0
L = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (i != k) and (j != k) :
                sum = i*100+j*10+k
                L.append(sum)
print(L)
print("这样的数共有：",len(L))

'''
网上做法
'''
#python自带这个函数的
from itertools import permutations

for i in permutations([1, 2, 3, 4], 3):
    print(i)