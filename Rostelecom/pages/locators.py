from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage

class Locators(AuthPage):
    '''Класс с локаторами, сообщениями и заголовками'''

    # Заголовок страницы авторизации
    TITLE_AUTH = 'Авторизация'

    LOCATOR_INPUT_MAIL = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    LOCATOR_BTN_MAIL = (By.ID, "t-btn-tab-mail")

    LOCATOR_INPUT_USERNAME = (By.ID, 'username')
    LOCATOR_INPUT_PASSWORD = (By.ID, 'password')

    LOCATOR_BTN_ENTER = (By.ID, 'kc-login')
    LOCATOR_BTN_LOGOUT = (By.ID, 'logout-btn')

    # Сообщение об ошибке при неверных данных
    ERROR_MSG_INVALID_DATA = 'Неверный логин или пароль'

    # Сообщение об ошибке
    LOCATOR_ERROR_MSG = (By.XPATH, "//span[@id='form-error-message']")

    # Кнопка 'Зарегистрироваться'
    LOCATOR_REGISTER = (By.XPATH, "//a[@id='kc-register']")
    # Заголовок страницы регистрации
    TITLE_REGISTRATION = 'Регистрация'
    # Заголовок страницы в правой части
    LOCATOR_PAGE_RIGHT = (By.XPATH, '//*[@id="page-right"]/div/div/h1')

    # Кнопка 'Вконтакте'
    LOCATOR_SOCIAL_NETWORK_VK = (By.ID, "oidc_vk")

    # Идентификатор 'Вход в VK ID'
    LOCATOR_IDENTIFIER_VK = (By.XPATH, "// div[contains(text(), 'Вход в VK ID')]")

    # Кнопка 'Одноклассники'
    LOCATOR_SOCIAL_NETWORK_OK = (By.ID, "oidc_ok")

    # Идентификатор 'Одноклассники'
    LOCATOR_IDENTIFIER_OK = (By.XPATH, "//div[contains(text(),'Одноклассники')]")

    # Кнопка 'Мой Мир@Mail.Ru'
    LOCATOR_SOCIAL_MAIL = (By.ID, "oidc_mail")

    # Идентификатор 'Мой Мир@Mail.Ru'
    LOCATOR_IDENTIFIER_MAIL = (By.XPATH, "// span[contains(text(), 'Мой Мир@Mail.Ru')]")

    # Кнопка 'Яндекс'
    LOCATOR_SOCIAL_YANDEX = (By.ID, "oidc_ya")

    # Идентификатор 'Яндекс'
    LOCATOR_IDENTIFIER_YANDEX = (By.XPATH, "//*[@id='UserEntryFlow']/form/div/div[1]/h1")

    # Активная вкладка 'Пользовательское соглашение'
    LOCATOR_AGREEMENT = (By.XPATH, "//a[@class='rt-link rt-link--orange' and @href='https://b2c.passport.rt.ru/sso-static/agreement/agreement.html']")
    # Идентификатор текста соглашения
    LOCATOR_AGREEMENT_ROOT = (By.ID, "root")

    # Кнопка 'Забыли пароль?'
    LOCATOR_FORGOT_PASSWORD = (By.ID, 'forgot_password')
    # Заголовок страницы восстановления пароля
    TITLE_RECOVERY = 'Восстановление пароля'

    # Сообщение об отсутствующем номере телефона
    EMPTY_PHONE_MSG = 'Введите номер телефона'
    # Сообщение об отсутствующем имени пользователя
    LOCATOR_EMPTY_USERNAME_MSG = (By.CSS_SELECTOR, '.rt-input-container__meta--error')
    # Кнопка 'Телефон'
    LOCATOR_BTN_PHONE = (By.ID, "t-btn-tab-phone")

    # Страница с регистрацией
    LOCATOR_INPUT_REGISTER_NAME = (By.NAME, 'firstName')
    LOCATOR_INPUT_REGISTER_SURNAME = (By.NAME, 'lastName')
    LOCATOR_INPUT_REGISTER_EMAIL = (By.ID, 'address')
    LOCATOR_INPUT_REGISTER_PASSWORD = (By.ID, 'password')
    LOCATOR_INPUT_REGISTER_CONFIRM_PASSWORD = (By.ID, 'password-confirm')
    LOCATOR_REGISTER_CLICK = (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]')
    LOCATOR_EMAIL_CONFIRM = (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/h1[1]')
    EMAIL_CONFIRM_MSG = 'Подтверждение email'
    LOCATOR_NAME_FAILED = (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]')
    NAME_FAILED_MSG = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'