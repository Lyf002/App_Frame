from testcase.baseTestCase import BaseTestCase
from pageobjects.home_page import HomePage
from pageobjects.base import BasePage
from framework.logger import Logger

logger=Logger(logger="Modify").getlog()
class Modify(BaseTestCase):
    """
    修改用户名测试用例
    """

    def test_modify(self):
        #登录
        home_page=HomePage(self.driver)
        base_page=BasePage(self.driver)
        # home_page.login("1593572580@qq.com","admin123")
        #修改用户名
        home_page.modify("admin")
        home_page.click(*home_page.button_back_loc)
        home_page.click(*home_page.button_topLeft_loc)
        rename_text=base_page.gettext(*home_page.preLogin_link_loc)
        try:
            self.assertEqual(rename_text, "admin")
            logger.info("用户名修改断言成功")
        except AssertionError as AE:
            logger.error("用户名修改断言失败")
            raise AE

