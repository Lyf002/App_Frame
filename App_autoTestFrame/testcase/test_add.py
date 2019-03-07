from testcase.baseTestCase import BaseTestCase
from pageobjects.home_page import HomePage
from pageobjects.base import BasePage
from framework.logger import Logger

logger=Logger(logger="Register").getlog()

class Add(BaseTestCase):
    """
    添加备忘录测试用例
    """
    def test_addBWL(self):
        home_page = HomePage(self.driver)
        base_page=BasePage(self.driver)
        home_page.add_bwl("BWL01","BWL02")
        firstBWL_text = base_page.gettext(*home_page.BWL02_text)
        secondBWL_text=base_page.gettext(*home_page.BWL01_text)
        try:
            self.assertEqual(firstBWL_text, "BWL02")
            self.assertEqual(secondBWL_text, "BWL01")
            logger.info("admin添加备忘录断言成功")
        except AssertionError as AE:
            logger.error("admin添加备忘录断言失败")
            raise AE

