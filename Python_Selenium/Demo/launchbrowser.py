import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select


class FillForm(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # Create new chrome session
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        # navigate to the application home page
        inst.driver.get("http://toolsqa.com/automation-practice-form/")
        inst.driver.title

    def test_enter_first_name(self):
        self.search_field = self.driver.find_element_by_css_selector("div input[name='firstname']")
        self.search_field.clear()
        self.search_field.send_keys("Test")

    def test_enter_last_name(self):
        self.search_field = self.driver.find_element_by_css_selector("div input[name='lastname']")
        self.search_field.clear()
        self.search_field.send_keys("Automation")

    def test_enter_date(self):
        self.search_field = self.driver.find_element_by_css_selector("div input[id='datepicker']")
        self.search_field.clear()
        self.search_field.send_keys("6/2/2018")

    def test_select_gender(self):
        self.search_field = self.driver.find_element_by_css_selector("input[value='Male']")
        #self.search_field.clear()
        self.search_field.click()

    def test_select_continents(self):
        self.driver.find_element_by_xpath("//*[@id='continents']//option[text()='Africa']").click()

    def test_click_on_partial_link(self):
        self.search_field = self.driver.find_element_by_css_selector("a[title='Automation Practice Form']")
        self.search_field.click()

    def test_click_on_partial_link(self):
        self.search_field = self.driver.find_element_by_css_selector("a[title='Automation Practice Form']")
        self.search_field.click()

    def test_click_on_submit_button(self):
        self.search_field = self.driver.find_element_by_css_selector("button[id='submit']")
        self.search_field.click()

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()
