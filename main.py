from controles import *
from selenium import webdriver
from acessos import LOGIN,SENHA,URL,CAMINHO, ANT_CAMINHO
from pastas import folder_canhotos,folder
import time
import pyautogui
import os

driver = webdriver.Chrome()
driver.get(URL)

#Acessando a pagina
driver.maximize_window()
driver.find_element('xpath','//*[@id="Usuario"]').send_keys(LOGIN)
driver.find_element('xpath','//*[@id="Senha"]').send_keys(SENHA)
driver.find_element('xpath','//*[@id="login-form"]/div[2]/div[3]/button').click()
time.sleep(3)
driver.find_element('xpath','//*[@id="js-nav-menu"]/li[6]/a').click()
driver.find_element('xpath','//*[@id="js-nav-menu"]/li[6]/ul/li[1]/a').click()
driver.find_element('xpath','//*[@id="js-nav-menu"]/li[6]/ul/li[1]/ul/li[1]/a').click()
time.sleep(2)
driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[4]/div/div/input').clear()
time.sleep(1.7)

def se_pendente(valor):
    driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr/td[13]/div/button').click()
    driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr/td[13]/div/div/a[4]').click()
    time.sleep(3)
    pyautogui.typewrite(f'{ANT_CAMINHO}\{valor}')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    print(f"------------{valor}-- ENVIADO PARA A DANONE ---------------------")

                  
def findCanhoto(canhoto):
    driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div/input').clear()
    driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(canhoto)
    driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[1]/div/div/div/div/div[3]/button[4]').click()
    time.sleep(2)
    pyautogui.press('pagedown')
    time.sleep(1)
    try:
        valor = driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr/td[1]').text
        status = driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr/td[8]').text
        if valor:
            if status == "Ag. Aprovação":
                print(f"O Canhoto {valor} encontrase com o status de: {str.upper(status)}")
                for canhoto in folder:
                    if canhoto == f'{valor}.png':
                        canhoto_Aguardando_Aprovacao(canhoto,f'{valor}.png')
                    if canhoto == f'{valor}.jpg':
                        canhoto_Aguardando_Aprovacao(canhoto,f'{valor}.jpg')
                        
            if status == "Digitalizado":
                print(f"O Canhoto {valor} encontrase com o status de: {str.upper(status)}")
                for canhoto in folder:
                    if canhoto == f'{valor}.png':
                        canhoto_digitalizado(canhoto,f'{valor}.png')
                    if canhoto == f'{valor}.jpg':
                        canhoto_digitalizado(canhoto,f'{valor}.jpg')
                    
            if status == "Pendente":
                print(f"O Canhoto {valor} encontrase com o status de: {str.upper(status)}")
                for canhoto in folder:
                    if canhoto == f'{valor}.png':
                        se_pendente(valor)
                        time.sleep(1)
                        canhoto_pendente(canhoto,f'{valor}.png')
                        
                    if canhoto == f'{valor}.jpg':
                        se_pendente(valor)
                        time.sleep(1)
                        canhoto_pendente(canhoto,f'{valor}.jpg')

            if status == "Rejeitada":
                print(f"O Canhoto {valor} encontrase com o status de: {str.upper(status)}")
                for canhoto in folder:
                    if canhoto == f'{valor}.png':
                        se_pendente(valor)
                        time.sleep(1)
                        canhoto_rejeitado(canhoto,f'{valor}.png')
                    if canhoto == f'{valor}.jpg':
                        se_pendente(valor)
                        time.sleep(1)
                        canhoto_rejeitado(canhoto,f'{valor}.jpg')
                    
            time.sleep(3)
        if not valor or ValueError:
            print('NAO ENCONTRADO')
    except Exception:
        print(f'{canhoto}------------NAO ENCONTRADO -----------------')
        arquivo_origem = os.path.join(CAMINHO,'CANHOTOS/',canhoto)
        arquivo_destino = os.path.join(CAMINHO,'CANHOTOS_NAO_ENCONTRADOS/',canhoto)
        os.rename(arquivo_origem, arquivo_destino)
        print(f'{canhoto}------------CANHOTO MOVIDO-----------------')
       
            
for item in folder_canhotos:
    print(f'-------Tentando encontrar o canhoto: {item}-------')
    findCanhoto(item)
    
print("FIM DA EXECUÇÃO")