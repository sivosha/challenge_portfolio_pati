import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.add_player_page import AddPlayer
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from PIL import Image

class TestDashboardPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_change_language_page(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user03@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()

        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.change_language()
        self.driver.save_screenshot("change_language.png")
        image = Image.open("change_language.png")

    def test_logout(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user03@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()

        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_log_out()

        user_login = LoginPage(self.driver)
        user_login.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()