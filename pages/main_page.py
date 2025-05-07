import allure
import pytest

from data import *
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Кликнуть на выпадающий список")
    def click_on_accordion(self, accordion_panel_number):
        accordion_panel_locator = MainPageLocators.accordion_panel_number(accordion_panel_number)
        self.scroll_to_element(accordion_panel_locator)
        self.click_on_element(accordion_panel_locator)

    @allure.step("Проверить текст выпадающего списка")
    def check_accordion_panel_text(self, accordion_panel_number):
        actual_text = self.get_text_on_element(MainPageLocators.accordion_panel_text(accordion_panel_number), 10)
        return actual_text == AccordionPanelText.accordion_text[accordion_panel_number]

    @allure.step("Кликнуть на кнопку Заказать вверху страницы")
    def click_to_order_button_top(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Кликнуть на кнопку Заказать внизу страницы")
    def click_to_order_button_bottom(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_BOTTOM)