from selenium.webdriver.chrome.service import Service
from pages.locators import Locators
from selenium import webdriver
from settings import driver_path
import pytest


@pytest.fixture()
def browser():
    """
    Функция-фикстура для инициализации браузера
    """

    driver = Service(driver_path)
    driver = webdriver.Chrome(service=driver)
    driver.maximize_window()
    yield driver
    driver.quit()


# создаем экземпляр класса, чтобы не создавать его в каждом тесте
@pytest.fixture()
def auth(browser):
    """
    Функция-фикстура для авторизации пользователя в приложении
    """
    auth = Locators(browser)
    return auth