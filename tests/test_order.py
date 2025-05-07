import pytest
import allure
from data import *

from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from locators.rent_page_locators import RentPageLocators
from pages.rent_page import RentPage


class TestOrder:
    @allure.title('Проверка заказа самоката')
    @pytest.mark.parametrize(
        'order_data, rent_period, color, locator' ,
        [
            (Data.order_data_1,RentPageLocators.RENT_PERIOD_1, RentPageLocators.COLOR_BLACK, OrderPageLocators.STATION_1),
            (Data.order_data_2,RentPageLocators.RENT_PERIOD_2, RentPageLocators.COLOR_GREY, OrderPageLocators.STATION_2)
        ]
    )
    def test_order_by_button_at_the_top(self, driver, order_data, rent_period, color, locator):
        main_page = MainPage(driver)
        main_page.click_to_order_button_top()
        order_page = OrderPage(driver)
        order_page.fill_order_form(**order_data, locator=locator)
        order_page.click_button_next_step()
        rent_page = RentPage(driver)
        rent_page.fill_rent_form(rent_period, color)
        rent_page.click_bottom_to_order_in_rent_form()
        rent_page.click_yes_to_order()
        response = rent_page.wait_for_element(RentPageLocators.ORDER_COMPLETE)
        assert response.is_displayed()



