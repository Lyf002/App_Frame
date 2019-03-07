from testcase.baseTestCase import BaseTestCase
from pageobjects.home_page import HomePage
from pageobjects.base import BasePage
from framework.logger import Logger

logger=Logger(logger="Register").getlog()
class GuiDang(BaseTestCase):
    """归档测试用例"""
    def test_guidnag(self):
        home_page = HomePage(self.driver)
        base_page=BasePage(self.driver)
        home_page.guidang()
        guidang_text = base_page.gettext(*home_page.BWL02_GD_text)
        try:
            self.assertEqual(guidang_text, "BWL02")
            logger.info("归档断言成功")
        except AssertionError as AE:
            logger.error("归档断言失败")
            raise AE

        home_page.huanYuan()
        huifu_text = base_page.gettext(*home_page.BWL02_GD_text)
        try:
            self.assertEqual(huifu_text, "BWL02")
            logger.info("还原备忘录断言成功")
        except AssertionError as AE:
            logger.error("还原备忘录断言失败")
            raise AE