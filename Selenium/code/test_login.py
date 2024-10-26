import time
import pytest
from _pytest.fixtures import FixtureRequest

import logindata
from base import BaseCase
from ui.pages.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from ui.locators import basic_locators


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.cresentials = credentials

        self.login_page = LoginPage(driver)
        self.locators = basic_locators.BasePageLocators()
        if self.authorize:
            print('Do something for login')


@pytest.fixture(scope='session')
def credentials():
        return {
            'email': logindata.email,
            'password': logindata.password
    }


@pytest.fixture(scope='function')
def cookies(driver, credentials):
    login_page = LoginPage(driver)
    login_page.login(credentials['email'], credentials['password'])

    WebDriverWait(driver, 10).until(
        EC.url_to_be(MainPage.url)
    )
    assert driver.current_url == MainPage.url, "URL не соответствует ожидаемому"

    cookies = driver.get_cookies()
    return cookies


class LoginPage(BasePage):
    url = 'https://education.vk.company/'

    
    def login(self, email, password):
        self.click(self.locators.AUTH_HEADER_BUTTON)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.SIGNUP_MODAL_LINK)
        ).click()
    
        email_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.EMAIL_INPUT)
        )
        email_elem.send_keys(email)
    
        password_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.PASSWORD_INPUT)
        )
        password_elem.send_keys(password)
    
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.LOGIN_BUTTON)
        ).click()


class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'


class TestLogin(BaseCase):
    authorize = True

    @pytest.mark.skip('skip')
    def test_login(self, credentials):
        self.login_page.login(credentials['email'], credentials['password'])

        WebDriverWait(self.login_page.driver, 10).until(
            EC.url_to_be(MainPage.url)
        )
        assert self.login_page.driver.current_url == MainPage.url, "URL не соответствует ожидаемому"

        assert 1 == 1


class TestLK(BaseCase):

    @pytest.mark.skip('skip')
    def test_lk2(self, cookies):
        self.driver.get(MainPage.url)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

        self.login_page.click(self.locators.SEARCH_BUTTON)

        
        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_page.locators.SEARCH_INPUT)
         )
        search_input.send_keys("Батовкин Александр")

        search_input.send_keys(Keys.ENTER)

        # Проверка
        found_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_page.locators.FOUND_NAME)
        ).text
        assert found_name == "Александр", f"Ожидалось имя 'Александр', но найдено '{found_name}'"
        found_last_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_page.locators.FOUND_LAST_NAME)
        ).text
        assert found_last_name == "Батовкин", f"Ожидалась фамилия 'Батовкин', но найдена '{found_last_name}'"

        time.sleep(2)

    # @pytest.mark.skip('skip')
    def test_lk3(self, cookies):
        self.driver.get(MainPage.url)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

        # зайти в расписание
        self.login_page.click(self.locators.SCHEDULE_BUTTON)

        time.sleep(2)
        # кнопка "Весь семестр"
        self.login_page.click(self.locators.SEMESTER_BUTTON)
        time.sleep(10)

        schedule_items = WebDriverWait(
            self.driver, 10).until(EC.presence_of_all_elements_located(self.locators.SCHEDULE_ITEM))

        for item in schedule_items:
            date_text = item.find_element(*self.locators.SCHEDULE_ITEM_DATE).text
            if date_text == "22 октября 2024":
                room_text = item.find_element(*self.locators.SCHEDULE_ITEM_ROOM).text
                assert room_text == " ауд.395 - зал 3 (МГТУ)", f"EОжидается ' ауд.395 - зал 3 (МГТУ)', но найдено'{room_text}'"
                break
        else:
            assert False, "Элемент с датой '22 октября 2024' не найден"
