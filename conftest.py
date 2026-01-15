import pytest
from selenium import webdriver
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
@pytest.fixture
def create_new_mail():
    mail = f"user{int(time.time())}@test.ru"
    return mail

@pytest.fixture
def create_bad_mail():
    mail = f"user{int(time.time())}"
    return mail

@pytest.fixture
def create_new_password():
    password = '123456789'
    return password

@pytest.fixture
def registered_user():
    creds = {'login': 'user333@mail.ru', 'password': '12345678'}
    return creds

@pytest.fixture
def desk_url():
    url = 'https://qa-desk.stand.praktikum-services.ru/'
    return url

