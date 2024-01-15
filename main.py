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
    time.sleep(3)
    driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[4]/div/div/div').click()
    driver.find_element('xpath','/html/body/div[4]/div[2]/div[2]').click()
    driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[4]/div/div/div').click()
    time.sleep(3)
    driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys('208411')
    driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[1]/div/div/div/div/div[3]/button[4]').click()
    time.sleep(3)
    valor = driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr/td[1]')
    time.sleep(3)
    if valor.text == "208411":
        status = driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr/td[12]')
        print(f"O Canhoto {valor.text} encontrase com o status {status.text}")
        
    
except Exception:
    print(Exception)
   