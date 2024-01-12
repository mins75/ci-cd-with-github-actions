import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By #Added
import chromedriver_autoinstaller

#import time

class TestAppE2E(unittest.TestCase):
    def setUp(self):
        # Launch your flask app first
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(executable_path=chromedriver_autoinstaller.install())
        self.driver.get('http://localhost:5000') 

    def test_add_and_delete_item(self):
        # you can use the driver to find elements in the page
        # example:
        """input_field = self.driver.find_element_by_name('item')"""
        input_field = self.driver.find_element(By.NAME, "item")
        # this refers to the 'name="item"' attribute of the html element
        # checkout the rest of the methods in the documentation:
        # https://selenium-python.readthedocs.io/locating-elements.html
        
        # after you select your element, you can send it a key press:
        input_field.send_keys("New E2E Item")
        input_field.send_keys(Keys.RETURN)
        """input_field.send_keys('New E2E Item')"""
        """input_field.send_keys(Keys.RETURN)"""
        
        # and you can use the rest of the assetion methods as well:
        self.assertIn("New E2E Item", self.driver.page_source)
        """self.assertIn('New E2E Item', self.driver.page_source)"""
        
        #Now test the update
        input_field = self.driver.find_element(By.NAME, "new_item")
        input_field.send_keys("Update E2E Item")
        input_field.send_keys(Keys.RETURN)
        self.assertIn("Update E2E Item", self.driver.page_source)
        self.assertNotIn("New E2E Item", self.driver.page_source) #Since the old item shouldn't be here anymore

        #Delete the item
        delete_element = self.driver.find_element(By.LINK_TEXT, "Delete")
        delete_element.send_keys(Keys.RETURN)
        self.assertNotIn("Update E2E Item", self.driver.page_source)
        #time.sleep(5) #to have a visual on the deletion

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
