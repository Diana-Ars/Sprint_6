import allure
import pytest

from data import *
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Заполнить форму заказа")
    def fill_order_form(self, name, surname, address, phone, station, locator):
        self.send_keys_to_input(OrderPageLocators.NAME, name)
        self.send_keys_to_input(OrderPageLocators.SURNAME, surname)
        self.send_keys_to_input(OrderPageLocators.ADDRESS, address)
        self.send_keys_to_input(OrderPageLocators.PHONE, phone)
        self.click_on_element(OrderPageLocators.STATION)
        self.send_keys_to_input(OrderPageLocators.STATION, station)
        self.click_on_element(locator)


    @allure.step("Кликнуть на кнопку Далее")
    def click_button_next_step(self):
        self.click_on_element(OrderPageLocators.NEXT_STEP)

