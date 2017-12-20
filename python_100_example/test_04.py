# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 22:34
# @Author  : zhaochencheng
# @QQ      : 907779487
# @version : Python 3.5.2
# @File    : test_04.py
# @Software: PyCharm Community Edition
'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
闰年：
①、普通年能被4整除且不能被100整除的为闰年.
②、世纪年能被400整除的是闰年
③、对于数值很大的年份,这年如果能整除3200,并且能整除172800则是闰年.如172800年是闰年,86400年不是闰年

判断闰年的方法：闰年满足两个条件（满足一个即为闰年）
1、能被4整除但不能被100整除
2、能被400整 除

'''
# def leapYear(year):
#
#     if year%100==0:
#         print("②、世纪年能被400整除的是闰年!")
#         date_year = 366
#     else:
#         if year %4 ==0 and year %100 !=0:
#             print("①、普通年能被4整除且不能被100整除的为闰年.")
#             date_year = 366
#         else:
#             print("平年")
#             date_year = 365
#
Year = int(input("请输入某年："))
while 1:

    month = int(input("请输入某月："))
    if 1<= month <= 12:
        while 1:
            day = int(input("请输入某日："))
            if 1<= day <= 31:
                print(Year,"年",month,"月",day,"日")
                break
            else:
                print("日期输入错误！！重新输入！")
                continue
        break
    else:
        print("月份输入错误！！重新输入！")
        continue
    # print(Year)
mon =[1,2,3,4,5,6,7,8,9,10,11,12]
mon_day = [0,31,28,31,30,31,30,31,31,30,31,30,31]
total = 0
if Year%100==0:
    # print("②、世纪年能被400整除的是闰年!%d"%Year)
    if month >= 3:
        total = 1
        for i in mon:
            if month >= (i):
                total = mon_day[i - 1] + total
        print("这一天是这一年的第%s天" % (total + day))
    else:
        for i in mon:
            if month >= (i):
                total = mon_day[i - 1] + total
        print("这一天是这一年的第%s天!" % (total + day))

    # date_year = 366
else:
    if Year%4 ==0 and Year %100 !=0:
        # print("①、普通年能被4整除且不能被100整除的为闰年,%d"%Year)
        # date_year = 366
        if month >= 3:
            total = 1
            for i in mon:
                if month >= (i):
                    total = mon_day[i - 1] + total
            print(total + day)
        else:
            for i in mon:
                if month >= (i):
                    total = mon_day[i - 1] + total
            print("这一天是这一年的第%s天!" % (total + day))

    else:
        # print("平年%d"%Year)
        for i in mon:
            if month >= (i):
                total = mon_day[i - 1] + total
        print("这一天是这一年的第%s天!" % (total + day))

        # date_year = 365
