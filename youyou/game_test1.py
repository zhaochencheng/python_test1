'''

猜数字游戏
'''
a = 1
b = 99
Key = 33
while 1:
    try:
        guess = int(input("请输入一个整数%d" %a +"到%d:" %b))
        if guess < Key and guess > a:
            a = guess
            print("请输入%d到" %a + "%d： " %b)
        elif guess> Key and guess < b:
            b = guess
            print("请输入%d到" %a + "%d： " %b)
        elif guess <= a or guess >= b:
            print("number is not in the range,please enter again!")
        elif guess == Key:
            print("number is right!")
            break
    except Exception as  e:
        print(e)
        print("Please enter a number!")