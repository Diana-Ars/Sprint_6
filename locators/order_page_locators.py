import pytest
from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_FORM = By.CLASS_NAME, 'Order_Content__bmtHS'
    NAME = By.XPATH, "//input[contains(@placeholder,'* Имя')]"
    SURNAME = By.XPATH, "//input[contains(@placeholder,'* Фамилия')]"
    ADDRESS = By.XPATH, "//input[contains(@placeholder,'* Адрес: куда привезти заказ')]"
    STATION = By.XPATH, "//input[contains(@placeholder,'* Станция метро')]"
    PHONE = By.XPATH, "//input[contains(@placeholder,'* Телефон: на него позвонит курьер')]"
    NEXT_STEP = By.XPATH, "//button[contains(text(), 'Далее')]"
    SELECT_STATION = By.XPATH, '//div[@class="select-search__select"]'
    STATION_1 = By.XPATH, '//button[@value="3"]'
    STATION_2 = By.XPATH, '//button[@value="47"]'
    LOGO_SCOOTER = By.XPATH, "//a[contains(@class,'Header_LogoScooter__3lsAR')]"
    LOGO_YANDEX = By.XPATH, "//a[contains(@class,'Header_LogoYandex__3TSOI')]"



