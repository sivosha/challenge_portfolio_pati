import time


from pages.base_page import BasePage




class Dashboard(BasePage):
    expected_title = 'Scouts panel'
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def find_user(self, user_name):
        time.sleep(1)
        assert self.find_element("//span[text()='" + user_name + "']")

    menu_main_page_xpath = "//*[contains(@d, 'M10')]/../../.."
    menu_players_xpath = "//*[contains(@d, 'M12 1')]/../../.."
    menu_language_xpath = "//*[contains(@d, 'M12.')]/../../.."
    menu_sign_out_xpath = "//*[contains(@d, 'M13')]/../../.."
    block_players_count_xpath = "//*[text()='Players count']/../div/b"
    block_matches_count_xpath = "//*[text()='Matches count']/../div/b"
    block_reports_count_xpath = "//*[text()='Reports count']/../div/b"
    block_events_count_xpath = "//*[text()='Events count']/../div/b"
    block_scouts_logo_xpath = "//*[contains(@title, 'Log')]"
    block_scouts_panel_xpath = "//p[contains(@class,'body2')]"
    link_devTeam_contact_xpath = "//*[contains(@class, 's-spacing')]"
    label_shortcuts_panel_xpath = "//*[text()='Shortcuts']"
    link_add_player_xpath = "//*[text()='Add player']/../.."
    link_last_created_player_xpath = "//*[text()='Last created player']/following-sibling::a[1]/button"
    link_last_updated_player_xpath = "//*[text()='Last updated player']/following-sibling::a[1]/button"
    link_last_created_match_xpath = "//*[text()='Last created match']/following-sibling::a[1]/button"
    link_last_updated_match_xpath = "//*[text()='Last updated match']/following-sibling::a[1]/button"
    link_last_updated_report_xpath = "//*[text()='Last updated report']/following-sibling::a[1]/button"
pass