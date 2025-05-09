import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helpers import *
from curl import *
from data import *
from locators.main_page_locators import *
from locators.order_page_locators import *
from pages.main_page import *
from pages.order_page import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture()
def driver():
    options = Options()
    browser = webdriver.Chrome(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()

