import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_success_login(self):
        #steps
        driver = self.browser
        driver.get("https://www.saucedemo.com/") #buka website
        time.sleep(3)
        driver.find_element(By.ID, "user-name").send_keys("standard_user") #isi email
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("secret_sauce") #isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        #validasi
        response_data = driver.find_element(By.CLASS_NAME, "title").text
        self.assertIn('PRODUCT', response_data)

    def test_failed_login_with_empty_password(self):
        #steps
        driver = self.browser
        driver.get("https://www.saucedemo.com/") #buka website
        time.sleep(3)
        driver.find_element(By.ID, "user-name").send_keys("standard_user") #email
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("") #password kosong
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        #validasi
        response_data = driver.find_element(By.CLASS_NAME, "error-message-container").text
        self.assertIn('Epic sadface: Password is required', response_data)
    
    def test_failed_login_with_empty_password_and_email(self):
        #steps
        driver = self.browser
        driver.get("https://www.saucedemo.com/") #buka website
        time.sleep(3)
        driver.find_element(By.ID, "user-name").send_keys("") #email kosong
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("") #password kosong
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        #validasi
        response_data = driver.find_element(By.CLASS_NAME, "error-message-container").text
        self.assertIn('Epic sadface: Username is required', response_data)
        
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
