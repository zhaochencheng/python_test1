# -*- coding: utf-8 -*-
# @Time    : 2017/12/24 21:14
# @Author  : zhaochencheng
# @QQ      : 907779487
# @version : Python 3.5.2
# @File    : baidushezhi_test04.py
# @Software: PyCharm Community Edition


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
try:
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    mouse = driver.find_element_by_link_text('设置')
    ActionChains(driver).move_to_element(mouse).perform()#鼠标悬停
    time.sleep(1)
    driver.find_element_by_link_text("搜索设置").click()
    time.sleep(3)
    # driver.quit()
    abc = driver.find_element_by_id("nr")
    # abc.find_element_by_xpath("//option[@value='50']").click()
    abc.find_element_by_xpath("//option[2]").click()
    driver.find_element_by_class_name("prefpanelgo").click() #保存设置
    time.sleep(2)
    a = driver.switch_to_alert()
    print(a.text)#alert 警示框
    a.accept()
    time.sleep(4)
    driver.quit()
except Exception as E:
    print(E)