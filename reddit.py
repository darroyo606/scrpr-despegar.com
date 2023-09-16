import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://reddit.com/")

login_button=driver.find_element(by=By.CSS_SELECTOR,value="#login-button")
login_button.click()
wait = WebDriverWait(driver, 30)
#time.sleep(20)
#username_input = driver.find_element(by=By.XPATH,value='//*[@id="loginUsername"]')
login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#loginButton')))
login_button.click()
username_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Nombre de usuario"]')))
password_input= driver.find_element(by=By.CSS_SELECTOR,value="#loginPassword")

username_input.send_keys('swing772')
password_input.send_keys('ciberseguridad.28')