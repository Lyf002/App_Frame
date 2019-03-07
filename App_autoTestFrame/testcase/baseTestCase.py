import unittest
from framework.apk_engine import ApkEngine

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        apk_eng=ApkEngine()
        self.driver=apk_eng.open_apk()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()