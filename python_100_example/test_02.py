# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 21:12
# @Author  : zhaochencheng
# @QQ      : 907779487
# @version : Python 3.5.2
# @File    : test_02.py
# @Software: PyCharm Community Edition
'''
题目：企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
'''
a = int(input("利润为(万)："))
total = 0
if a >=100:
    total = (a-100)*0.01+(100-60)*0.015+(60-40)*0.03+(40-20)*0.05+(20-10)*0.075+10*0.1
    print("奖金为：",total*10000)
elif 60<=a<100:
    total =  (a - 60) * 0.015 + (60 - 40) * 0.03 + (40 - 20) * 0.05 + (20 - 10) * 0.075 + 10 * 0.1
    print("奖金为：",total * 10000)
elif 40<=a<60:
    total = (a - 40) * 0.03 + (40 - 20) * 0.05 + (20 - 10) * 0.075 + 10 * 0.1
    print("奖金为：",total * 10000)
elif 20<=a<40:
    total = (a - 20) * 0.05 + (20 - 10) * 0.075 + 10 * 0.1
    print("奖金为：",total * 10000)
elif 10<=a<20:
    total = (a - 10) * 0.075 + 10 * 0.1
    print("奖金为：",total * 10000)
elif 0<=a<10:
    total =  a * 0.1
    print("奖金为：",total * 10000)
'''
网上答案
Python中的列表可以嵌套，这样外层列表就跟数组一样，内层的是对象；
不过Python的列表数据类型不一定一样，更加灵活了。
'''
Bonus = 0;
BonusRateList = [[100,0.010],[60,0.015],[40,0.030],[20,0.050],[10,0.075],[0,0.100]];

Profit =  int(input("利润为(万)："))
# Profit = 10000;

for i in range(0, len(BonusRateList)) :
    if (Profit > BonusRateList[i][0]) :
        Bonus += ((Profit - BonusRateList[i][0]) * BonusRateList[i][1]);
        Profit = BonusRateList[i][0];

print ("奖金为：",Bonus * 10000);
