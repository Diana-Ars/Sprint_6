import allure
import pytest

from data import *
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.dzen_page_locators import DzenPageLocators



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

    @allure.step("Подождать загрузку формы заказа")
    def wait_for_order_form(self):
        self.wait_for_element(OrderPageLocators.ORDER_FORM)

    @allure.step("Кликнуть на логотип Самокат")
    def click_to_logo_scooter(self):
        self.click_on_element(OrderPageLocators.LOGO_SCOOTER)

    @allure.step("Кликнуть на логотип Яндекс и подождать открытие вкладки-Дзен")
    def wait_for_open_dzen(self):
        self.wait_for_open_new_window(OrderPageLocators.LOGO_YANDEX)

    @allure.step("Переход на вкладку Дзен")
    def switch_to_window_dzen(self):
        self.switch_to_new_window()

    @allure.step("Подождать загрузку Дзен-страницы")
    def wait_for_visibility_dzen(self):
        self.wait_for_element(DzenPageLocators.DZEN)
        return self.driver.find_element(*DzenPageLocators.DZEN)




