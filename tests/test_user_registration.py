import pytest
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
        expected_conditions.presence_of_element_located(EMAIL_INPUT))
    
    driver.find_element(*EMAIL_INPUT).send_keys(create_new_mail)
    driver.find_element(*PASSWORD_INPUT).send_keys(create_new_password)
    driver.find_element(*SUBMIT_PASSWORD_INPUT).send_keys(create_new_password)
    
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
        expected_conditions.presence_of_element_located(EMAIL_INPUT))
    
    driver.find_element(*EMAIL_INPUT).send_keys(create_bad_mail)
    driver.find_element(*PASSWORD_INPUT).send_keys(create_new_password)
    driver.find_element(*SUBMIT_PASSWORD_INPUT).send_keys(create_new_password)
    
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(CREATE_ACCOUNT_BUTTON))
    driver.find_element(*CREATE_ACCOUNT_BUTTON).click()