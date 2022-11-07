from pages.base_page import BasePage


class Dashboard(BasePage):
    menu_main_page_xpath="//*[contains(@d, 'M10')]/../../.." #"//div[contains(@class, 'jss43')]/.."
    menu_players_xpath="//*[contains(@d, 'M12 1')]/../../.."
    menu_test_test_xpath="//*[contains(@d, 'M13.')]/../../.."
    menu_matches_xpath="//*[contains(@d, '2C6')]/../../parent::div"
    menu_reports_xpath = "//*[contains(@d, 'M19')]/../../.."
    menu_language_xpath="//*[contains(@d, 'M12.')]/../../.."
    menu_sign_out_xpath="//*[contains(@d, 'M13 3')]/../../.."
    input_my_team_xpath="//*[@name='myTeam']"
    input_enemy_team_xpath="//*[@name='enemyTeam']"
    input_my_team_score_xpath="//*[@name='myTeamScore']"
    input_enemy_team_score_xpath="//*[@name='enemyTeamScore']"
    input_date_xpath="//*[@name='date']"
    radio_match_at_home="//div[@role='radiogroup']/label[1]"    #//*[text()='Match at home']/../span[1]
    radio_match_out_home="//div[@role='radiogroup']/label[2]"
    input_tshirt_xpath="//*[@name='tshirt']"
    input_league_xpath="//*[@name='league']"
    input_time_played_xpath="//*[@name='timePlayed']"
    input_number_xpath="//*[@name='number']"
    input_web_match_xpath="//*[@name='webMatch']"
    input_general_xpath="//*[@name='general']"
    input_rating_xpath="//*[@name='rating']"
    btn_submit_xpath="//*[@type='submit']"
    btn_clear_xpath="//div[contains(@class, 'MuiCard')]/*[@type='button']"

pass