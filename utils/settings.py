import os
import sys

from selenium.webdriver.common.by import By

SYSTEM = sys.platform
PATH_TO_PROJECT = os.path.dirname(os.path.abspath(__file__))

if SYSTEM == 'win32':
    CHROME_DRIVER = "chromedriver.exe"
else:
    CHROME_DRIVER = "chromedriver"

DRIVER_PATH = os.path.join(PATH_TO_PROJECT, '../drivers', CHROME_DRIVER)
IMPLICITLY_WAIT = 3
EXPLICITLY_WAIT = 30

DEFAULT_LOCATOR_TYPE = By.XPATH


UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"

if SYSTEM == 'windows':
    CHROME_DRIVER = 'chromedriver.exe'
    FIREFOX_DRIVER = 'geckodriver.exe'
    EDGE_DRIVER = 'MicrosoftWebDriver.exe'
else:
    CHROME_DRIVER = 'chromedriver'
    FIREFOX_DRIVER = 'geckodriver'
    EDGE_DRIVER = 'MicrosoftWebDriver.exe'
