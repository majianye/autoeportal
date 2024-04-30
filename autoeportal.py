
import time
from selenium.webdriver.common.keys import Keys
import keyboard
from selenium import webdriver
driver = webdriver.Chrome(r'D:\pythonProject_AUTOEPORTAL\chromedriver.exe')
time.sleep(2)
# 打开登录网页
driver.get("http://eportal.hhu.edu.cn/") #  10.96.0.155
#登录账号 无加密，可send
time.sleep(1)
driver.find_element_by_id('username').send_keys('220402020004', Keys.TAB) #自己的账号
time.sleep(1)
#登录密码 加密不能send，模拟键盘操作
keyboard.write("Mjy!19980712")
time.sleep(1)
#选择出口
driver.find_element_by_id('xiala').click()
driver.find_element_by_id('_service_1').click()
time.sleep(1)
#记住密码
driver.find_element_by_class_name('disPlayIs_check').click()
time.sleep(1)
#点击登录
driver.find_element_by_id('loginLink_div').click()
time.sleep(3)
driver.quit()
