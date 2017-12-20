# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 23:43
# @Author  : zhaochencheng
# @QQ      : 907779487
# @version : Python 3.5.2
# @File    : test_05.py
# @Software: PyCharm Community Edition
'''

题目：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，
如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
'''
L = [23,3,1,44,55,21]
List= [23,3,1,44,55,21]
# for i in (input(),''):
#     L.append(i)
# print(L)
# j = 1
# i = j= k = 0

length =len(L)
print(length)
# for b in range(0,length):
#     print(L[b])
# for i in range(0,length-1):
#     if L[i]>L[i+1]:
#         k = L[i]
#         L[i]= L[i+1]
#         L[i+1]= k
# length -=1
while length > 0:
    for i in range(0, length - 1):
        if List[i] > List[i + 1]:
            a = List[i]
            List[i] = List[i + 1]
            List[i + 1] = a
    # print(length)
    length -= 1
print(L)
print(List)