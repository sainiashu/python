import unittest
from selenium import webdriver

class AlertTest(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # Create new chrome session
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        # navigate to the application home page
        inst.driver.get("http://toolsqa.com/handling-alerts-using-selenium-webdriver/")
        inst.driver.title

    def test_sample_alert(self):
        self.search_field = self.driver.find_element_by_css_selector("p button[onclick='pushAlert()']")
        self.search_field.click()

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__=='__main__':
    unittest.main()