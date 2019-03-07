from framework.logger import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time
import os

logger=Logger(logger='BasePage').getlog()
class BasePage(object):

    def __init__(self,driver):
        self.driver=driver

    def get_screenshot(self):
        file_path=os.path.dirname(os.path.abspath('.'))+'/screenshots/'
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        rq=time.strftime(('%Y%m%d%H%M'),time.localtime(time.time()))
        img_name=file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(img_name)
            logger.info("截图成功")
        except Exception as e:
            self.get_screenshot()
            logger.error("截图失败！")

    def find_element(self,*loc):
        """定位页面元素"""
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            logger.info("%s找到页面元素%s" % (self, loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            self.get_screenshot()
            logger.error("%s页面元素未找到--%s" % (self, loc))

    def clear(self,*loc):
        """清除文本框内容"""
        element = self.find_element(*loc)
        try:
            element.clear()
            logger.info("%s清除%s文本框内容"% (self, loc))
        except Exception as e:
            self.get_screenshot()
            logger.error("清除内容失败！")

    def sendkeys(self,text,*loc):
        """在文本框中输入内容"""
        element=self.find_element(*loc)
        try:
            element.send_keys(text)
            logger.info("%s输入%s"%(self,loc))
        except Exception as e:
            self.get_screenshot()
            logger.error("%s输入失败！%s"%(self,loc))

    def click(self,*loc):
        """单击事件"""
        element = self.find_element(*loc)
        try:
            element.click()
            logger.info("%s点击%s"%(self,loc))
        except Exception as e:
            self.get_screenshot()
            logger.error("%s单击失败%s！"%(self,loc))

    def gettext(self,*loc):
        """获取元素相应的文本信息"""
        element=self.find_element(*loc)
        try:
            return element.text
            logger.info("%s获取%s文本" %(self,loc))
            print(element.text)
        except Exception as e:
            self.get_screenshot()
            logger.error("%s获取文本失败%s"%(self,loc))

    def longPress(self,*loc):
        """长按某一页面元素"""
        element = self.find_element(*loc)
        try:
            touch=TouchAction(self.driver)
            touch.long_press(element).wait(2000).perform()
            logger.info("%s长按%s" % (self, loc))
        except Exception as e:
            self.get_screenshot()
            logger.error("%s长按失败！%s" % (self, loc))

    def swipeLeft(self,x1,y1,x2,y2,duration):
        self.driver.swipe(x1,y1,x2,y2,duration)

    def swipeDown(self,x1,y1,x2,y2,duration):
        self.driver.swipe(x1,y1,x2,y2,duration)

