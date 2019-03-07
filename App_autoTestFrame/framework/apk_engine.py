from appium import webdriver
import os
import yaml
from framework.logger import Logger

logger=Logger(logger='ApkEngine').getlog()

class ApkEngine():
     apk_path = os.path.dirname(os.path.abspath("."))
     print(apk_path)
     def open_apk(self):
        with open(self.apk_path+'/config/config.yaml','r',encoding='utf-8')as file:
            data=yaml.load(file)
        # 创建一个字典
        desried_cap = {}
        desried_cap['platformName'] = data['platformName']  # 设备系统
        desried_cap['platformVersion'] = data['platformVersion']  # 被测系统版本
        desried_cap['deviceName'] = data['deviceName']  # 设备名称
        desried_cap['sessionOverride'] = data['sessionOverride']  # 每次创建新的session

        app_path=self.apk_path + r'\app\znbwl.apk'
        desried_cap['app'] = app_path
        desried_cap['noReset'] = data['noReset']

        # # 应用程序包名
        # desried_cap['appPackage'] = 'com.pdswp.su.smartcalendar'
        # desried_cap['appActivity'] = 'com.example.todolist.LoginActivity'

        # 实例driver
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desried_cap)
        return driver

# if __name__=="__main__":
#     ApkEngine()
