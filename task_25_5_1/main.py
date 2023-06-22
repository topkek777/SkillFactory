import pytest
from selenium import webdriver
from settings import valid_email, valid_password, driver_path, base_url
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# !Используется старая версия Selenium (v.3.14.1)!
driver = webdriver.Chrome(driver_path)

@pytest.fixture(autouse=True, scope='class')
def testing():

    # Переходим на страницу авторизации
    driver.get(f'{base_url}/login')
    wait = WebDriverWait(driver, 1)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@type="submit"]')))
    # Вводим email
    driver.find_element_by_id('email').send_keys(valid_email)
    # Вводим пароль
    driver.find_element_by_id('pass').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element_by_css_selector('button[type="submit"]').click()

    yield

    driver.quit()


class TestPetFriends:
    '''Проверки сайта PetFriends'''

    def test_show_my_pets(self):
       '''Попадаем на главную страницу пользователя'''

       assert driver.find_element_by_tag_name('h1').text == "PetFriends"

    def test_all_pets_are_visible(self):
        '''На странице со списком питомцев пользователя: присутствуют все питомцы.'''

        driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="all_my_pets"]')))
        cards = driver.find_elements(By.CSS_SELECTOR, 'tbody>tr')
        statistics = driver.find_element(By.CSS_SELECTOR, 'div.task3 div')
        amount = statistics.text.split(': ')
        amount_of_pets = int(amount[1][:amount[1].find('\n')])
        assert len(cards) == int(amount_of_pets)

    def test_pets_have_photo(self):
        '''На странице со списком питомцев пользователя: хотя бы у половины питомцев есть фото.'''

        driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class=".col-sm-4 left"]/h2')))
        images = driver.find_elements(By.CSS_SELECTOR, 'img')
        statistics = driver.find_element(By.CSS_SELECTOR, 'div.task3 div')
        amount = statistics.text.split(': ')
        amount_of_pets = int(amount[1][:amount[1].find('\n')])
        count = 0
        for i in range(len(images)):
            if images[i].get_attribute('src') != '':
                count += 1
        assert count > amount_of_pets // 2

    def test_pets_have_name_age_breed(self):
        '''На странице со списком питомцев пользователя: у всех питомцев есть имя, возраст и порода.'''

        driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
        driver.implicitly_wait(5)
        descriptions = driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets table tbody tr')
        for i in range(len(descriptions)):
            parts = descriptions[i].text.split(' ')
            if len(parts) >= 3:
                assert len(parts[0]) > 0
                assert len(parts[1]) > 0
                assert len(parts[2]) > 0

    def test_pets_have_unique_names(self):
        '''На странице со списком питомцев пользователя: у всех питомцев разные имена.'''

        driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
        driver.implicitly_wait(5)
        names = driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets table tbody tr')
        pet_name = []
        for i in range(len(names)):
            parts = names[i].text.split(' ')
            pet_name.append(parts[0])
        for i in range(len(pet_name) - 1):
            for j in range(i + 1, len(pet_name)):
                assert pet_name[i] != pet_name[j]

    def test_all_pets_are_unique(self):
        '''На странице со списком питомцев пользователя: в списке нет повторяющихся питомцев. (Сложное задание)'''

        driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
        driver.implicitly_wait(5)
        descriptions = driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets table tbody tr')
        animals = []
        unique_animals = []
        for i in range(len(descriptions)):
            temp = descriptions[i].text.split(' ')
            if len(temp) >= 2:
                animals.append(temp)

        for i in animals:
            if i not in unique_animals:
                unique_animals.append(i)

        assert len(animals) == len(unique_animals)