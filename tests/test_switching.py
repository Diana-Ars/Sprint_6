import pytest
import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from locators.dzen_page_locators import DzenPageLocators


class TestSwitching:
    @allure.title("Проверка перехода на главную страницу через клик на логотип Самокат")
    def test_switching_to_main_page_by_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_order_button_top()
        order_page = OrderPage(driver)
        order_page.wait_for_element(OrderPageLocators.ORDER_FORM)
        order_page.click_on_element(OrderPageLocators.LOGO_SCOOTER)
        response = main_page.wait_for_element(MainPageLocators.MAIN_PAGE)
        assert response.is_displayed()

    @allure.title("Проверка перехода на страницу Дзен через клик на логотип Яндекс")
    def test_switching_to_dzen_by_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_order_button_top()
        order_page = OrderPage(driver)
        order_page.wait_for_element(OrderPageLocators.ORDER_FORM)
        windows = driver.window_handles
        order_page.click_on_element(OrderPageLocators.LOGO_YANDEX)
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > len(windows))
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(DzenPageLocators.DZEN)
        )
        assert driver.find_element(*DzenPageLocators.DZEN)


