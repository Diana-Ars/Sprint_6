import pytest
from selenium.webdriver.common.by import By


class DzenPageLocators:
    DZEN = By.XPATH, "//header[contains(@class, 'dzen-layout--desktop-base-header__header-11 dzen-layout--desktop-base-header__isMorda-2n')]"

