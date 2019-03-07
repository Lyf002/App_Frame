from testcase.baseTestCase import BaseTestCase
from pageobjects.home_page import HomePage
class Search(BaseTestCase):
    """
    搜索测试用例
    """
    def test_search(self):
        home_page = HomePage(self.driver)
        home_page.search("w")
        home_page.noSet()
