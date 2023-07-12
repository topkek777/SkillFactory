from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import base_url


class AuthPage:

    def __init__(self, driver):
        """ Конструктор класса AuthPage. """
        self.driver = driver
        self.base_url = base_url

    def go_to_site(self):
        """ Переход на базовый URL веб-сайта. """
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        """ Поиск элемента на странице с использованием заданного локатора. (макс. время ожидания элемента 10 секунд """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator), message=f"Не удалось найти элемент по локатору {locator}"
        )

    def click_element(self, locator):
        """ Нажатие на элемент по заданному локатору """
        self.find_element(locator).click()

    def input_data(self, locator, text):
        """ Ввод текста в поле ввода, найденного по заданному локатору. """
        self.find_element(locator).send_keys(text)