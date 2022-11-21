from pages.base_page import BasePage


class AddPlayer(BasePage):
    login_field_xpath = "//input[@id='login']"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()= 'Sign in']"
    expected_title = 'Scouts panel - sign in'
    title_of_box_xpath = "//h5[text()='Scouts Panel']"
    add_name_xpath = "//*[@name ='name']"
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    add_surname_xpath = "//*[@name ='surname']"
    add_age_xpath = "//*[@name ='age']"
    add_main_position_xpath = "//*[@name ='mainPosition']"
    submit_button_xpath = "//*[@type='submit']"
    expected_add_player_title = 'Add player'

    def title_of_page(self):
        assert self.get_page_title(self.add_player_url) == self.expected_add_player_title

    def type_in_name(self, name):
        self.field_send_keys(self.add_name_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.add_surname_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.add_age_xpath, age)

    def type_in_position(self, pos):
        self.field_send_keys(self.add_main_position_xpath, pos)

    def click_on_the_add_player_button(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        self.click_on_the_element(self.submit_button_xpath)


    def title_of_add_player_page(self):
        assert self.get_page_title(self.login_url) == self.expected_add_player_title
