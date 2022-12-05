import os
import time
import unittest
from lib2to3.pgen2 import driver

from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

from PIL import Image



class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.title_of_box()
        user_login.type_in_email('user03@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()

        self.driver.save_screenshot("login_to_the_system.png")
        image = Image.open("login_to_the_system.png")


    def test_login_with_invalid_data (self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.title_of_box()
        user_login.type_in_email('user03@ getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        user_login.error_message_is_visible()
        self.driver.save_screenshot("Invalid_login_to_the_system.png")
        image = Image.open("Invalid_login_to_the_system.png")

    def test_dropdown_language(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.title_of_box()
        title = user_login.get_element_text(user_login.get_password_reminder)
        is_polski = user_login.get_element_text(user_login.drop_down_language) == 'Polski'
        user_login.click_on_the_element(user_login.drop_down_language)
        user_login.find_element(user_login.drop_down_language)  ##Popup doesn't show up without this execution

        if is_polski:
            user_login.click_on_the_element(user_login.li_english)
        else:
            user_login.click_on_the_element(user_login.li_polski)
        assert title != user_login.get_element_text(user_login.get_password_reminder)

        self.driver.save_screenshot("drop_down_language.png")
        image = Image.open("drop_down_language.png")

    @classmethod
    def tearDown(self):
        self.driver.quit()
