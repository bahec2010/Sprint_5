import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from locators import *

def test_card_creation_by_unregestered_user(driver, desk_url):
    driver.get(desk_url)
    
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(LOGIN_AND_REGISTRATION_BUTTON))
    driver.find_element(*POST_ADVERTISEMENT).click()
    
    WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located(POPUP_LOGIN_TO_POST_ADVERTISEMENT))
    
    popup = driver.find_element(*POPUP_LOGIN_TO_POST_ADVERTISEMENT)
    assert popup.is_displayed()

    driver.quit()


def test_card_creation_by_regestered_user(driver, desk_url, create_new_mail, create_new_password):
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
    driver.find_element(*POST_ADVERTISEMENT).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(NAME_OF_CARD))
    driver.find_element(*NAME_OF_CARD).send_keys("Test card")
    driver.find_element(*DESCRIPTION_OF_CARD).send_keys("Test description")
    driver.find_element(*COST_OF_CARD).send_keys("100")
    driver.find_element(*CATEGORY_DROPDOWN_OPEN).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(BOOKS_CATEGORY))
    driver.find_element(*BOOKS_CATEGORY).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(NAME_OF_CARD))
    driver.find_element(*SECOND_HAND_RADIO_BUTTON).click()
    driver.find_element(*TO_PUBLISH_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(THREE_COLOUMNS))
    profile_element = driver.find_element(*USER_PHOTO)
    driver.execute_script("arguments[0].scrollIntoView();", profile_element)

    driver.find_element(*USER_PHOTO).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(MY_ADVERTISEMENT_CARD))
    
    element = driver.find_element(*MY_ADVERTISEMENT_CARD)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located(MY_ADVERTISEMENT_CARD))
    assert element.is_displayed()


    
    