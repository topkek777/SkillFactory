from settings import *
import pytest


# TC-RTK-001 Страница авторизации успешно открывается
def test_authorization_is_exists(auth):
    auth.go_to_site()
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_AUTH

# TC-RTK-002 Открывается форма авторизации по почте
def test_mail_is_clickable(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    assert auth.find_element(auth.LOCATOR_INPUT_MAIL)

# TC-RTK-003 Успешная авторизация по валидным номеру телефона и паролю
# TC-RTK-004 Успешная авторизация по валидным почте и паролю
@pytest.mark.parametrize('username', [valid_phone, valid_email], ids=['valid phone', 'valid email'])
def test_auth_valid_data(auth, username):
    auth.go_to_site()
    if username == valid_phone:
        auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    else:
        auth.click_element(auth.LOCATOR_BTN_MAIL)
        auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)

# TC-RTK-005 Успешная авторизация по невалидному номеру телефона и валидному паролю
# TC-RTK-006 Успешная авторизация по невалидной почте и валидному паролю
@pytest.mark.parametrize('username', [invalid_phone, invalid_email], ids=['invalid phone', 'invalid email'])
def test_auth_fake_password(auth, username):
    auth.go_to_site()
    if username == invalid_phone:
        auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    else:
        auth.click_element(auth.LOCATOR_BTN_MAIL)
        auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_ERROR_MSG).text == auth.ERROR_MSG_INVALID_DATA

# TC-RTK-007 Страница регистрации успешно открывается
def test_register(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_REGISTER)
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_REGISTRATION

# TC-RTK-008 Доступен переход на страницу авторизации через ВКонтакте
def test_auth_social_network_vk(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_SOCIAL_NETWORK_VK)
    assert auth.find_element(auth.LOCATOR_IDENTIFIER_VK)

# TC-RTK-009 Доступен переход на страницу авторизации через Одноклассники
def test_auth_social_network_ok(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_SOCIAL_NETWORK_OK)
    assert auth.find_element(auth.LOCATOR_IDENTIFIER_OK)

# TC-RTK-010 Доступен переход на страницу авторизации через mail.ru
def test_auth_social_mail(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_SOCIAL_MAIL)
    assert auth.find_element(auth.LOCATOR_IDENTIFIER_MAIL)

# TC-RTK-011 Доступен переход на страницу авторизации через Yandex
def test_auth_social_yandex(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_SOCIAL_YANDEX)
    assert auth.find_element(auth.LOCATOR_IDENTIFIER_YANDEX)

# TC-RTK-012 Доступен переход на страницу пользовательского соглашения
def test_agreement_is_clickable(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_AGREEMENT)
    windows = auth.driver.window_handles
    auth.driver.switch_to.window(windows[-1])
    assert auth.find_element(auth.LOCATOR_AGREEMENT_ROOT)

# TC-RTK-013 Доступен переход к странице восстановления пароля
def test_forgot_password(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_FORGOT_PASSWORD)
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_RECOVERY

# TC-RTK-014 Неуспешная авторизация по пустому телефону и валидному паролю
# TC-RTK-015 Неуспешная авторизация по пустому телефону и пустому паролю
@pytest.mark.parametrize('password', [valid_password, ''], ids=['valid password', 'invalid empty password'])
def test_auth_empty_phone(auth, password):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_PHONE)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_PHONE_MSG

# TC-RTK-016 Регистрация с валидным именем (5 символов - положительный класс эквивалентности)
# TC-RTK-017 Регистрация с валидным именем (30 символов - правое граничное значение)
# TC-RTK-018 Регистрация с невалидным именем (31 символ - правый негативный класс эквивалентности)
# TC-RTK-019 Регистрация с валидным именем (2 символа - левое граничное значение)
# TC-RTK-020 Регистрация с невалидным именем (1 символ - левый негативный класс эквивалентности)
@pytest.mark.parametrize('name', [valid_name, valid_name*6, valid_name*6 + 'д', 'Ян', 'Я'],
                         ids=['5 символов', '30 символов', '31 символ', '2 символа', '1 символ'])
def test_register_email_positive(auth, name):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_REGISTER)
    auth.input_data(auth.LOCATOR_INPUT_REGISTER_NAME, valid_name)
    auth.input_data(auth.LOCATOR_INPUT_REGISTER_SURNAME, valid_surname)
    auth.input_data(auth.LOCATOR_INPUT_REGISTER_EMAIL, valid_email)
    auth.input_data(auth.LOCATOR_INPUT_REGISTER_PASSWORD, valid_password)
    auth.input_data(auth.LOCATOR_INPUT_REGISTER_CONFIRM_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_REGISTER_CLICK)
    if 2 <= len(name) <= 30:
        assert auth.find_element(auth.LOCATOR_EMAIL_CONFIRM).text == auth.EMAIL_CONFIRM_MSG
    else:
        assert auth.find_element(auth.LOCATOR_NAME_FAILED).text == auth.NAME_FAILED_MSG

