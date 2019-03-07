from testcase.baseTestCase import BaseTestCase
from pageobjects.home_page import HomePage
from pageobjects.base import BasePage
from framework.util import Util
from ddt import ddt,data,unpack
from framework.logger import Logger

logger=Logger(logger="Register").getlog()

#读取表格数据
testdata=Util.read_excel("D:\Appium_TestFrame\App_autoTestFrame\web\loginBook.xlsx","Sheet1")
print(testdata)

@ddt
class UserLogin(BaseTestCase):

    """
    登录测试用例
    """
    @data(*testdata)
    def test_login(self,data):
        home_page=HomePage(self.driver)
        base_page=BasePage(self.driver)
        home_page.click(*home_page.button_topLeft_loc)
        home_page.click(*home_page.preLogin_link_loc)
        uname=data["userName"]
        upwd=data["password"]
        print("userName:",uname)
        print("password:",upwd)
        home_page.relogin(uname,upwd)

        home_page.click(*home_page.button_topLeft_loc)
        home_page.click(*home_page.preLogin_link_loc)
        username_text = base_page.gettext(*home_page.preLogin_link_loc)
        try:
            self.assertEqual(username_text, "admin001")
            logger.info("admin登录断言成功")
        except AssertionError as AE:
            logger.error("admin登录断言失败")
            raise AE
