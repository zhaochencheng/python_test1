# -*- coding: utf-8 -*-
# @Time    : 2017/12/17 22:50
# @Author  : zhaochencheng
# @QQ      : 907779487
# @version :Python 3.5.2
# @File    : 水仙花_test3.py
# @Software: PyCharm Community Edition
'''
1、如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。  
例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数

那么问题来了，求1000以内的水仙花数（3位数）

'''
def shuixianhuashu(b):
    c = b
    L = []
    #求b 有几个数位
    length = len(str(b))
    length2 = len(str(b))

    #将b 数位分解----将百 十 个 位数 存放到列表L 中
    i = 0
    for j in range(0, length):
        i = b // (10 ** (length - 1))
        # print(i)
        L.append(i)
        b = b - i * (10 ** (length - 1))
        length -= 1
    # print(L)

    # 求数位拆分后；每个数位的幂和 与 原数是否相同----是否为水仙花数
    total = 0
    for k in range(0, length2):
        total = L[k] ** length2 + total
    # print("total:", total)
    if total == c:
        print("%d 是水仙花数！" % c)
    else:
        # print("%d 不是水仙花数！" % c)
        pass

if __name__ == '__main__':
    # shuixianhuashu(153)
    for i in range(100, 1000):
        shuixianhuashu(i)

    #执行上述程序 所用时间
    # start = time.time()
    # '''code you want to time goes here'''
    # # for i in range(100, 1000):
    # #     shuixianhuashu(i)
    # end = time.time()
    # elapsed = end - start
    # print ("Time taken: ", elapsed, "seconds")
'''
网上学习  优： 程序简单， 执行速度快 ，运行时间短；
'''
#如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
#例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数。
# for i in range(10,10000):
#     sum=0 #各个位数的立方和
#     temp=i
#     while temp !=0:
#         sum=sum+(temp%10)**3   #累加
#         temp//=10   #地板除
#     if sum==i:
#         print(i)


