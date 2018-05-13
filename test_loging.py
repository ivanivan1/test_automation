from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import unittest

path_to_chrome_driver = "C:\\Users\\User\\Desktop\\test_automation\chromedriver.exe"
chrome_driver = webdriver.Chrome(path_to_chrome_driver)
hudl_login_url = "https://www.hudl.com/login"
hudl_log_in_title = "Log In - Hudl"
hudl_home_title = "Home - Hudl"
email_account = "serafimov_ivan@yahoo.com"
password_account = "Seavus135"
email_id = "email"
password_id = "password"
log_in_id = "logIn"
timeout_login = 5

class LogInTest(unittest.TestCase):
    def test_login(self):
        email = None
        password = None
        log_in = None
        self.driver = chrome_driver
        self.driver.get(hudl_login_url)
        self.assertIn(hudl_log_in_title, self.driver.title, "Failed to load:%s" % hudl_log_in_title)
        try:
            email = self.driver.find_element_by_id(email_id)
        except NoSuchElementException:
            with self.assertRaises(NoSuchElementException):
                self.driver.quit()
                raise Exception("Element %s not found" % email_id)
        try:
            password = self.driver.find_element_by_id(password_id)
        except NoSuchElementException:
            with self.assertRaises(NoSuchElementException):
                self.driver.quit()
                raise Exception("Element %s not found" % password_id)
        try:
            log_in = self.driver.find_element_by_id(log_in_id)
        except NoSuchElementException:
            with self.assertRaises(NoSuchElementException):
                self.driver.quit()
                raise Exception("Element %s not found" % log_in_id)
        email.send_keys(email_account)
        password.send_keys(password_account)
        log_in.click()
        try:
            title_present = ec.title_is(hudl_home_title)
            WebDriverWait(self.driver, timeout_login).until(title_present)
            self.driver.close()
        except TimeoutException:
            with self.assertRaises(TimeoutException):
                if self.driver.find_element_by_class_name("login-error-container"):
                    self.driver.close()
                    raise Exception("Login error")
                else:
                    self.driver.close()
                    raise Exception("Timeout login to:%s" % hudl_home_title)


if __name__ == '__main__':
    unittest.main()