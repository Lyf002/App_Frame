from testcase.baseTestCase import BaseTestCase
from pageobjects.home_page import HomePage
class Order(BaseTestCase):
    """排序测试用例"""
    def test_order(self):
        home_page = HomePage(self.driver)
        home_page.order()