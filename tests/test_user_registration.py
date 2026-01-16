import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *

def test_user_registration(driver, desk_url, create_new_mail, create_new_password):
    driver.get(desk_url)
    
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(LOGIN_AND_REGISTRATION_BUTTON))
    driver.find_element(*LOGIN_AND_REGISTRATION_BUTTON).click()
    
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(NO_ACCOUNT_BUTTON))
    driver.find_element(*NO_ACCOUNT_BUTTON).click()
    
    WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located(REGISTRATION_EMAIL_INPUT))
    
    driver.find_element(*REGISTRATION_EMAIL_INPUT).send_keys(create_new_mail)
    driver.find_element(*REGISTRATION_PASSWORD_INPUT).send_keys(create_new_password)
    driver.find_element(*REGISTRATION_SUBMIT_PASSWORD_INPUT).send_keys(create_new_password)
    
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(CREATE_ACCOUNT_BUTTON))
    driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(PROFILE_NAME))

    profile_name_element = driver.find_element(*PROFILE_NAME)
    assert 'User' in profile_name_element.text

    driver.quit()

def test_user_registration_with_bad_email(driver, desk_url, create_bad_mail, create_new_password):
    driver.get(desk_url)
    
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(LOGIN_AND_REGISTRATION_BUTTON))
    driver.find_element(*LOGIN_AND_REGISTRATION_BUTTON).click()
    
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(NO_ACCOUNT_BUTTON))
    driver.find_element(*NO_ACCOUNT_BUTTON).click()
    
    WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located(REGISTRATION_EMAIL_INPUT))
    
    driver.find_element(*REGISTRATION_EMAIL_INPUT).send_keys(create_bad_mail)
    driver.find_element(*REGISTRATION_PASSWORD_INPUT).send_keys(create_new_password)
    driver.find_element(*REGISTRATION_SUBMIT_PASSWORD_INPUT).send_keys(create_new_password)
    
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(CREATE_ACCOUNT_BUTTON))
    driver.find_element(*CREATE_ACCOUNT_BUTTON).click()
    
    
    WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located(RED_ERROR_MESSAGE))
    
    error_message_element = driver.find_element(*RED_ERROR_MESSAGE)
    assert 'Ошибка' in error_message_element.text
    
    error_email_input = driver.find_element(*RED_INPUT_EMAIL)
    error_password_input = driver.find_element(*RED_INPUT_PASSWORD)
    error_submit_password_input = driver.find_element(*RED_INPUT_SUBMIT_PASSWORD)
    
    assert error_email_input is not None
    assert error_password_input is not None
    assert error_submit_password_input is not None
    
    driver.quit()



def test_registered_user_registration(driver, desk_url, registered_user):
    driver.get(desk_url)
    
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(LOGIN_AND_REGISTRATION_BUTTON))
    driver.find_element(*LOGIN_AND_REGISTRATION_BUTTON).click()
    
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(NO_ACCOUNT_BUTTON))
    driver.find_element(*NO_ACCOUNT_BUTTON).click()
    
    WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located(REGISTRATION_EMAIL_INPUT))
    
    driver.find_element(*REGISTRATION_EMAIL_INPUT).send_keys(registered_user['login'])
    driver.find_element(*REGISTRATION_PASSWORD_INPUT).send_keys(registered_user['password'])
    driver.find_element(*REGISTRATION_SUBMIT_PASSWORD_INPUT).send_keys(registered_user['password'])

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(CREATE_ACCOUNT_BUTTON))
    driver.find_element(*CREATE_ACCOUNT_BUTTON).click()
    
    
    WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located(RED_ERROR_MESSAGE))
    
    error_message_element = driver.find_element(*RED_ERROR_MESSAGE)
    assert 'Ошибка' in error_message_element.text
    
    error_email_input = driver.find_element(*RED_INPUT_EMAIL)
    error_password_input = driver.find_element(*RED_INPUT_PASSWORD)
    error_submit_password_input = driver.find_element(*RED_INPUT_SUBMIT_PASSWORD)
    
    assert error_email_input is not None
    assert error_password_input is not None
    assert error_submit_password_input is not None
    
    driver.quit()