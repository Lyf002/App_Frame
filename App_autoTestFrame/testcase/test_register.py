from testcase.baseTestCase import BaseTestCase
from pageobjects.home_page import HomePage
from pageobjects.base import BasePage
from framework.logger import Logger

logger=Logger(logger="Register").getlog()
class Register(BaseTestCase):
    """注册测试用例"""

    def test_register_fail(self):
        home_page = HomePage(self.driver)
        base_page=BasePage(self.driver)
        home_page.regist()
        home_page.reg_sendkeys("admin", "1593572580@qq.com", "1234567")
        registFail_text=base_page.gettext(*home_page.registerFail_text_loc)
        try:
            self.assertEqual(registFail_text,"注册中……")
            logger.info("注册失败断言成功")
        except AssertionError as AE:
            logger.error("注册失败断言失败")
            raise AE


    def test_register_success(self):
        home_page=HomePage(self.driver)
        base_page = BasePage(self.driver)
        home_page.regist()
        home_page.reg_sendkeys("admin", "15935722@126.com", "1234567")
        home_page.click(*home_page.button_topLeft_loc)
        username_text=base_page.gettext(*home_page.preLogin_link_loc)
        try:
            self.assertEqual(username_text,"admin")
            logger.info("注册成功断言成功")
        except AssertionError as AE:
            logger.error("注册成功断言失败")
            raise AE
        home_page.click(*home_page.preLogin_link_loc)
        home_page.click(*home_page.logout_link_loc)
