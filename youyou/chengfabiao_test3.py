# -*- coding: utf-8 -*-
# @Time    : 2017/12/17 22:39
# @Author  : zhaochencheng
# @QQ      : 907779487
# @File    : chengfabiao_test3.py
# @Software: PyCharm Community Edition
'''
可参考  打印不同格式的9*9乘法表；
https://www.cnblogs.com/suiy-160428/p/5594389.html
'''
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*"%i+"%d"%j+"=%d "%(i*j),end="")
    print()
# print(1*4)