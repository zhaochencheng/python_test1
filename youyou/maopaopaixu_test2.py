# -*- coding: utf-8 -*-
# @Time    : 2017/12/17 21:42
# @Author  : zhaochencheng
# @Site    : 
# @File    : maopaopaixu_test2.py
# @Software: PyCharm Community Edition
'''
冒泡排序
'''
def maopao(List):
    length = len(List)
    while length >0:
        for i in range(0,length-1):
            if List[i] > List[i+1]:
                a = List[i]
                List[i] = List[i+1]
                List[i+1] = a
        # print(length)
        length -= 1
    print(List1)
if __name__ == '__main__':
    List1 = [3, 2, 1, 9, 10, 78, 6]
    maopao(List1)
