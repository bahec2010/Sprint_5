import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *


def test_user_login(driver, desk_url, registered_user):
    driver.get(desk_url)
    
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(LOGIN_AND_REGISTRATION_BUTTON))
    driver.find_element(*LOGIN_AND_REGISTRATION_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(EMAIL_INPUT))
    driver.find_element(*EMAIL_INPUT).send_keys(registered_user['login'])
    driver.find_element(*PASSWORD_INPUT).send_keys(registered_user['password'])
    driver.find_element(*LOGIN_BUTTON).click()

    
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(USER_PHOTO))

    profile_name_element = driver.find_element(*PROFILE_NAME)
    user_photo = driver.find_element(*USER_PHOTO)
    assert 'User' in profile_name_element.text
    assert user_photo.is_displayed()

    driver.quit()




def test_user_logout(driver, desk_url, registered_user):
    driver.get(desk_url)
    
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(LOGIN_AND_REGISTRATION_BUTTON))
    driver.find_element(*LOGIN_AND_REGISTRATION_BUTTON).click()
    
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(EMAIL_INPUT))
    driver.find_element(*EMAIL_INPUT).send_keys(registered_user['login'])
    driver.find_element(*PASSWORD_INPUT).send_keys(registered_user['password'])
    driver.find_element(*LOGIN_BUTTON).click()

    
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(PROFILE_NAME))
    driver.find_element(*LOGOUT_BUTTON).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(LOGIN_AND_REGISTRATION_BUTTON))
    
    WebDriverWait(driver, 3).until(
        expected_conditions.invisibility_of_element_located(PROFILE_NAME))
    WebDriverWait(driver, 3).until(
        expected_conditions.invisibility_of_element_located(USER_PHOTO))

    assert len(driver.find_elements(*PROFILE_NAME)) == 0
    assert len(driver.find_elements(*USER_PHOTO)) == 0
    assert driver.find_element(*LOGIN_AND_REGISTRATION_BUTTON).is_displayed()
    
    driver.quit()