import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestSwitching:
    @allure.title("Проверка перехода на главную страницу через клик на логотип Самокат")
    def test_switching_to_main_page_by_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_order_button_top()
        order_page = OrderPage(driver)
        order_page.wait_for_order_form()
        order_page.click_to_logo_scooter()
        current_page = main_page.wait_for_main_page()
        assert current_page.is_displayed()

    @allure.title("Проверка перехода на страницу Дзен через клик на логотип Яндекс")
    def test_switching_to_dzen_by_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_order_button_top()
        order_page = OrderPage(driver)
        order_page.wait_for_order_form()
        order_page.wait_for_open_dzen()
        order_page.switch_to_window_dzen()
        response = order_page.wait_for_visibility_dzen()
        assert response.is_displayed()


