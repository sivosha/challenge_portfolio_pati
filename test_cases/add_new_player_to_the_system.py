import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.add_player_page import AddPlayer
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from PIL import Image

class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user03@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()

        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()

        player_name = 'Player'
        player_surname = 'Surname'
        player_age = '07/07/2007'
        player_position = 'goalkeeper'
        previous_club = 'none'

        add_player = AddPlayer(self.driver)
        add_player.title_of_page()
        add_player.type_in_name(player_name)
        add_player.type_in_surname(player_surname)
        add_player.type_in_age(player_age)
        add_player.type_in_position(player_position)
        add_player.type_in_previous_club(previous_club)
        add_player.click_on_the_add_player_button()

        dashboard_page.find_user(player_name + ' ' + player_surname)

        self.driver.save_screenshot("added_player.png")
        image = Image.open("added_player.png")
        image.show()
    @classmethod
    def tearDown(self):
        self.driver.quit()
