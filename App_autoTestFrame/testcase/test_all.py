# import sys
# sys.path.append('D:\Appium_TestFrame\App_autoTestFrame')

from testcase.test_register import Register
from testcase.test_login import UserLogin
from testcase.test_modifyUname import Modify
from testcase.test_add import Add
from testcase.test_search import Search
from testcase.test_order import Order
from testcase.test_guidang import GuiDang
from testcase.test_delete import Delete
import os
import time
import unittest
import HTMLTestRunner

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.'))+ '/repoter/'
if not os.path.exists(report_path):
    os.mkdir(report_path)

now=time.strftime(('%Y-%m-%d-%H_%M_%S'),time.localtime(time.time()))
html_repoter = report_path +now+"_result.html"
fp = open(html_repoter, "wb")

# 构造测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Register))
suite.addTest(unittest.makeSuite(UserLogin))
suite.addTest(unittest.makeSuite(Modify))
suite.addTest(unittest.makeSuite(Add))
suite.addTest(unittest.makeSuite(Search))
suite.addTest(unittest.makeSuite(GuiDang))
suite.addTest(unittest.makeSuite(Order))
suite.addTest(unittest.makeSuite(Delete))

if __name__ == "__main__":
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="APP测试报告", description="用例执行情况")
    runner.run(suite)
