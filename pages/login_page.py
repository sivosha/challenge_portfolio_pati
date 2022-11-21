from lib2to3.pgen2 import driver

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    login_field_xpath = "//input[@id='login']"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()= 'Sign in']"

    expected_title = 'Scouts panel - sign in'
    header_of_box = 'Scouts Panel'
    get_password_reminder = "//a"

    header_of_box_xpath = '//h5'
    invalid_credentials_xpath = "//*[contains(@class, 'caption')]"
    drop_down_language = "//*[@aria-haspopup='listbox']"
    li_english = "//*[@data-value = 'en']"
    li_polski = "//*[@data-value = 'pl']"

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.wait_for_element_to_be_clickable(self.sign_in_button_xpath)
        self.click_on_the_element(self.sign_in_button_xpath)

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def title_of_box(self):
        self.assert_element_text(self.driver, self.header_of_box_xpath, self.header_of_box)

    def error_message_is_visible(self):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'caption')]")))


    def select_drop_down_language(self, xpath):
        self.visibility_of_element_located(xpath)
        selected = driver.find_element_by_xpath(xpath)
pass
