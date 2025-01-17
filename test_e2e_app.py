import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By #Added
#import chromedriver_autoinstaller

#import time

class TestAppE2E(unittest.TestCase):
    def setUp(self):
        # Launch your flask app first
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://localhost:5000') 
    

    def test_add_and_delete_item(self):
        #self.driver.get("http://127.0.0.1:5000")
        input_field = self.driver.find_element(By.NAME, "item")
        input_field.send_keys("New E2E Item")
        input_field.send_keys(Keys.RETURN)
        self.assertIn("New E2E Item", self.driver.page_source)
        input_field = self.driver.find_element(By.NAME, "new_item")
        input_field.send_keys("Update E2E Item")
        input_field.send_keys(Keys.RETURN)
        self.assertIn("Update E2E Item", self.driver.page_source)
        self.assertNotIn("New E2E Item", self.driver.page_source)
        delete_element = self.driver.find_element(By.LINK_TEXT, "Delete")
        delete_element.send_keys(Keys.RETURN)
        self.assertNotIn("Update E2E Item", self.driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
