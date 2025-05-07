import pytest
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta


class RentPageLocators:
    RENT_FORM = By.CLASS_NAME, 'Order_Content__bmtHS'
    RENT_DATA = By.XPATH, "//input[contains(@placeholder,'* Когда привезти самокат')]"
    RENT_PERIOD = By.XPATH, "//div[contains(text(), '* Срок аренды')]"
    RENT_PERIOD_1 = By.XPATH, "//div[contains(text(), 'трое суток')]"
    RENT_PERIOD_2 = By.XPATH, "//div[contains(text(), 'сутки')]"
    COLOR = By.CLASS_NAME, 'Order_Checkboxes__3lWSI'
    RENT_BUTTON = By.XPATH, "//button[contains(@class,'Button_Button__ra12g Button_Middle__1CSJM') and contains(text(), 'Заказать')]"
    SELECT_PERIOD = By.CLASS_NAME, 'Dropdown-menu'
    COLOR_BLACK = By.ID, 'black'
    COLOR_GREY = By.ID, 'grey'
    FINISH_ORDER = By.CLASS_NAME, 'Order_Modal__YZ-d3'
    BUTTON_YES = By.XPATH, '//button[contains(text(), "Да")]'
    ORDER_COMPLETE = By.XPATH, '//div[contains(text(), "Заказ оформлен")]'

    @staticmethod
    def select_data():
        tomorrow = datetime.now() + timedelta(days=1)
        day = tomorrow.day
        day_str = f"{day:02}"
        return By.XPATH, f"//div[@class='react-datepicker__day react-datepicker__day--0{day_str}']"
