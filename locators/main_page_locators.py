import pytest
from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE = By.XPATH, "//div[contains(@class, 'Home_FirstPart__3g6vG')]"
    ORDER_BUTTON_TOP = By.CLASS_NAME, 'Button_Button__ra12g'
    ORDER_BUTTON_BOTTOM = By.CLASS_NAME,'Button_Button__ra12g Button_Middle__1CSJM'

    @staticmethod
    def accordion_panel_number(accordion):
        return By.ID, f'accordion__heading-{accordion}'

    @staticmethod
    def accordion_panel_text(accordion):
        return By.ID, f'accordion__panel-{accordion}'

