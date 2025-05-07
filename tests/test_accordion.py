import pytest
import allure

from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestAccordion:
    @allure.title('Проверка текста в выпадающем списке "Вопросы о важном"')
    @pytest.mark.parametrize('accordion_number', range(8))
    def test_accordion(self, driver, accordion_number ):
        main_page = MainPage(driver)
        main_page.wait_for_element(MainPageLocators.MAIN_PAGE, 7)
        main_page.click_on_accordion(accordion_number)
        assert main_page.check_accordion_panel_text(accordion_number)

