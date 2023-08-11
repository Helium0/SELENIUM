import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage


class LoginTest(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        time.sleep(5)
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        time.sleep(2)

        # self.driver.find_element(By.NAME, 'username').send_keys('Admin')
        # self.driver.find_element(By.NAME, 'password').send_keys('admin123')
        # self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span').click()
        # self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()
        # time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")
