from selenium import webdriver
from senha import LOGIN,SENHA,URL
import time

driver = webdriver.Chrome()

driver.get(URL)

try:
    driver.maximize_window()
    driver.find_element('xpath','//*[@id="Usuario"]').send_keys(LOGIN)
    driver.find_element('xpath','//*[@id="Senha"]').send_keys(SENHA)
    time.sleep(2)
    driver.find_element('xpath','//*[@id="login-form"]/div[2]/div[3]/button').click()
    time.sleep(3)
    driver.find_element('xpath','//*[@id="js-nav-menu"]/li[6]/a').click()
    driver.find_element('xpath','//*[@id="js-nav-menu"]/li[6]/ul/li[1]/a').click()
    driver.find_element('xpath','//*[@id="js-nav-menu"]/li[6]/ul/li[1]/ul/li[1]/a').click()
    time.sleep(5)
        
except Exception:
    print(Exception)
   