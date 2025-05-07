import allure
import pytest

from pages.base_page import BasePage
from locators.rent_page_locators import RentPageLocators


class RentPage(BasePage):
    @allure.step("Заполнить форму аренды")
    def fill_rent_form(self, locator1, locator2):
        self.click_on_element(RentPageLocators.RENT_DATA)
        self.click_on_element(RentPageLocators.select_data())
        self.click_on_element(RentPageLocators.RENT_PERIOD)
        self.wait_for_element(RentPageLocators.SELECT_PERIOD)
        self.click_on_element(locator1)
        self.click_on_element(locator2)

    @allure.step("Кликнуть на кнопку 'Заказать' в форме аренды")
    def click_bottom_to_order_in_rent_form(self):
        self.click_on_element(RentPageLocators.RENT_BUTTON)

    @allure.step("Кликнуть кнопку 'Да' в окне 'Хотите оформить заказ?'")
    def click_yes_to_order(self):
        self.wait_for_element(RentPageLocators.FINISH_ORDER)
        self.click_on_element(RentPageLocators.BUTTON_YES)





