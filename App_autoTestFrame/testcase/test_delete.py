from testcase.baseTestCase import BaseTestCase
from pageobjects.home_page import HomePage
class Delete(BaseTestCase):
    """删除备忘录测试用例"""
    def test_delete(self):
        home_page=HomePage(self.driver)
        home_page.delete()