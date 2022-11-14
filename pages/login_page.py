from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//input[@id='login']"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()= 'Sign in']"
    expected_title = 'Scouts panel - sign in'
    header_of_box = 'Scouts Panel'
    header_of_box_xpath = '//h5'

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def title_of_box(self):
        self.assert_element_text(self.driver, self.header_of_box_xpath, self.header_of_box)
pass
