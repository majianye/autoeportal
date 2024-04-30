# autoeportal
hhu校园网自动认证（远程防断网）
```python
#所需第三方库
import time
from selenium.webdriver.common.keys import Keys
import keyboard
from selenium import webdriver
```
1. 设置chomedriver调用路径，**注意chorme的版本与chomedriver的版本需要适应**，选择相近的版本号即可。[chorme历史版本](https://www.chromedownloads.net/chrome64win/); [chormedriver版本](https://www.chromedownloads.net/chrome64win/)。\
**另外注意彻底关闭chorme自动更新。**[关闭chorme自动更新](https://blog.csdn.net/weixin_48337566/article/details/123242827)。
```python
#设置chomedriver调用路径
driver = webdriver.Chrome(r'D:\pythonProject_AUTOEPORTAL\chromedriver.exe')
time.sleep(2)
```
2. 打开登录网页
```python
# 打开登录网页
driver.get("http://eportal.hhu.edu.cn/") #  10.96.0.155
time.sleep(2)
```
3. 输入个人信息
```python
#登录账号 无加密，可send
time.sleep(1)
driver.find_element_by_id('username').send_keys('user’s name', Keys.TAB) #自己的账号
time.sleep(1) #设置等待时间，等待交互
#登录密码 加密不能send，模拟键盘操作
keyboard.write("user's PWD")
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
```
4. 打包形成可执行程序，**在程序根文件夹启动cmd后运行即可**\
**其中，D:\pythonProject_AUTOEPORTAL\favicon_logosc\favicon.ico，为可执行程序图标文件路径。
```cmd
pyinstaller -F -p D:\python311\lib\site-packages -i D:\pythonProject_AUTOEPORTAL\favicon_logosc\favicon.ico autoeportal.py
```
5. 将打包形成的可执行程序加入到计算机事件或系统自启动文件夹即可\
