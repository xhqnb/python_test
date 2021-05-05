import unittest

import ddt as ddt
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

T=0.5
@ddt.ddt
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost/phpwind/admin.php")
        time.sleep(T)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    @ddt.file_data(r"C:\Users\xhq\PycharmProjects\bbsTest\data\LoginDate.json")
    @ddt.unpack
    def test_Login(self,loginDate):
        name, password = loginDate.split(":")
        self.driver.find_element_by_xpath("//*[@id=\"wrapc\"]/div/form/table/tbody/tr[1]/td/div/input").clear()
        self.driver.find_element_by_xpath("//*[@id=\"wrapc\"]/div/form/table/tbody/tr[1]/td/div/input").send_keys(name)
        self.driver.find_element_by_xpath("//*[@id=\"wrapc\"]/div/form/table/tbody/tr[2]/td/div/input").clear()
        self.driver.find_element_by_xpath("//*[@id=\"wrapc\"]/div/form/table/tbody/tr[2]/td/div/input").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id=\"wrapc\"]/div/form/table/tbody/tr[3]/td/input").click()
        time.sleep(T)
        self.assertIn("注销",self.driver.page_source)
    # def test_something(self):
    #     self.assertEqual(True, False)

    @ddt.file_data(r"C:\Users\xhq\PycharmProjects\bbsTest\data\AddType.json")
    @ddt.unpack
    def test_addType(self,typeDate):
        self.driver.find_element_by_xpath("//*[@id=\"setforum\"]").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[2]/td/form/input[3]").send_keys(typeDate)
        self.driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[2]/td/form/input[4]").click()
        time.sleep(T)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/center/input[1]").click()
        time.sleep(T)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr/td[2]/form/a").click()
        time.sleep(T)
        self.driver.switch_to.parent_frame()

    @ddt.file_data(r"C:\Users\xhq\PycharmProjects\bbsTest\data\\AddPlate.json")
    @ddt.unpack
    def test_add(self,plateDate):
        type_,content=plateDate.split(":")
        plates=content.split(",")
        for plate in plates:
            # print(plate)
            self.driver.switch_to.frame("main")
            self.driver.find_element_by_xpath("//*[@id=\"forum_form\"]/input[4]").send_keys(plate)
            time.sleep(T)
            select1=Select(self.driver.find_element_by_xpath("//*[@id=\"forum_form\"]/select"))
            select1.select_by_visible_text(">> "+type_)
            self.driver.find_element_by_xpath("//*[@id=\"forum_form\"]/input[6]").click()
            time.sleep(T)
            self.driver.find_element_by_xpath("/html/body/div[1]/form/center/input[1]").click()
            time.sleep(T)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr/td[2]/form/a").click()
            time.sleep(T)
            self.driver.switch_to.parent_frame()
            self.driver.find_element_by_xpath("//*[@id=\"setforum\"]").click()



if __name__ == '__main__':
    unittest.main()
