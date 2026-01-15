import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *

def test_card_creation(driver, desk_url, create_new_mail, create_new_password):
    driver.get(desk_url)
    
    # Login first
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(LOGIN_AND_REGISTRATION_BUTTON))
    driver.find_element(*LOGIN_AND_REGISTRATION_BUTTON).click()
    
    WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located(EMAIL_INPUT))
    
    driver.find_element(*EMAIL_INPUT).send_keys(create_new_mail)
    driver.find_element(*PASSWORD_INPUT).send_keys(create_new_password)
    
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(LOGIN_BUTTON))
    driver.find_element(*LOGIN_BUTTON).click()
    
    # Create a new card
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(ADD_CARD_BUTTON))
    driver.find_element(*ADD_CARD_BUTTON).click()
    
    # Add card details
    WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located(CARD_NAME_INPUT))
    
    driver.find_element(*CARD_NAME_INPUT).send_keys("Test Card")
    driver.find_element(*CARD_DESCRIPTION_INPUT).send_keys("Test Description")
    
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(SAVE_CARD_BUTTON))
    driver.find_element(*SAVE_CARD_BUTTON).click()
    
    # Verify card was created
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located(CARD_ITEM))
    
    card_elements = driver.find_elements(*CARD_ITEM)
    assert len(card_elements) > 0
    
    driver.quit()