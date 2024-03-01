import unittest
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
from dotenv import load_dotenv
load_dotenv()
import os

MAX_WAIT = 5

class NewVisitorTest(unittest.TestCase):  

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException):
                if time.time() - start_time > MAX_WAIT:
                    raise
                time.sleep(0.5)

    def setUp(self):  
        self.browser = webdriver.Firefox()  

    def tearDown(self):  
        self.browser.quit()

    def test_browser_home(self):  
        self.browser.get("http://localhost:8000")  

        self.assertIn("Home", self.browser.title)  
        self.assertIn("You are not logged in", self.browser.page_source)  

        self.browser.find_element(By.XPATH, '//*[@href="/accounts/login/"]')
        self.browser.find_element(By.XPATH, '//*[@href="/signup/"]')

    def test_login(self):
        self.browser.get("http://localhost:8000")  

        self.browser.find_element(By.XPATH, '//*[@href="/accounts/login/"]').click()
        self.wait_for(
                lambda: self.browser.find_element(By.XPATH, '//*[@name="username"]')
        )
        inputbox = self.browser.find_element(By.XPATH, '//*[@name="username"]')
        inputbox.send_keys(os.environ.get('TEST_EMAIL'))
        passwordbox = self.browser.find_element(By.XPATH, '//*[@name="password"]')
        passwordbox.send_keys(os.environ.get('TEST_EMAIL_PASSWORD'))
        submitbutton = self.browser.find_element(By.XPATH, '//*[@type="submit"]')
        time.sleep(0.5)
        submitbutton.send_keys(Keys.ENTER)
        self.wait_for(
            lambda: self.assertIn("Hi pcarrie@incwo.com!", self.browser.page_source)
        )
        time.sleep(0.5)



if __name__ == "__main__":  
    unittest.main()  
