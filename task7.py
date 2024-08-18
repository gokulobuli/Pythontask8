from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

try:

    driver.get("https://www.imdb.com/search/name/")


    wait = WebDriverWait(driver, 10)


    name_input = wait.until(EC.presence_of_element_located((By.NAME, 'name')))
    name_input.send_keys('Tom Hanks')


    sort_dropdown = wait.until(EC.presence_of_element_located((By.NAME, 'sort')))
    sort_dropdown.send_keys('Birth Date')


    gender_dropdown = wait.until(EC.presence_of_element_located((By.NAME, 'gender')))
    gender_dropdown.send_keys('Male')


    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Search"]')))
    search_button.click()

finally:
    driver.quit()
