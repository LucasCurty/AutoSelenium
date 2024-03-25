from controles import *
from selenium import webdriver
from acessos import LOGIN,SENHA,URL,CAMINHO, CAMINHO_ENV
from pastas import create_folders, rename_arquivos
import time
import pyautogui
import os

#caminho dos arquivos
caminho_origem = os.listdir(f'{CAMINHO}CANHOTOS')
#renomeando canhotos
lista_canhotos = rename_arquivos()
#----------iniciando aplicação
print("INICIANDO AUTOMAÇÃO !\n")
print("CONFERINDO PASTAS...\n")
create_folders() # verificando pastas

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

#função para enviar o canhoto pendente
def se_pendente(valor): 
    driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr/td[13]/div/button').click()
    driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr/td[13]/div/div/a[4]').click()
    time.sleep(3)
    pyautogui.typewrite(f'{CAMINHO_ENV}\{valor}.png')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    print(f"==== {valor}-- ENVIADO PARA A DANONE ")
        
#função inicial para gerenciar entre pastas
def gerenciando_canhoto(canhoto,status_canhoto):
    if status_canhoto == 'Pendente':
        se_pendente(canhoto)
    else:    
        try:
            print(f"==== O canhoto {canhoto} está com o status: {status_canhoto.upper()}")
            arquivo_origem = os.path.join(f'{CAMINHO}CANHOTOS/',f'{canhoto}.png')
            arquivo_destino = os.path.join(f'{CAMINHO}/CANHOTOS_{status_canhoto.upper()}/',f'{canhoto}.png')
            os.rename(arquivo_origem, arquivo_destino)
            print(f"==== Canhoto movido para: {arquivo_destino}")
        except Exception as error:
            print(error)
            
def verificando_afundo(valor):
    driver.find_element('/html/body/div[2]/div/div/main/section/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[2]/div/div/div[2]/button')
    time.sleep(2)
    driver.find_element('/html/body/div[2]/div/div/main/div[20]/div/div/div[2]/form/div[2]/div/div/input').send_keys(valor)
    driver.find_element('/html/body/div[2]/div/div/main/div[20]/div/div/div[2]/div[1]/div/button')
    time.sleep(2)
    resultado = driver.find_element('/html/body/div[2]/div/div/main/div[20]/div/div/div[2]/div[3]/div[1]/div/div/table/tbody/tr/td[6]/span').text
    driver.find_element('/html/body/div[2]/div/div/main/div[20]/div/div/div[1]/button/span/i')
    return resultado
        
def findCanhoto(canhoto):
    driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div/input').clear()
    driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(canhoto)
    driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[1]/div/div/div/div/div[3]/button[4]').click()
    time.sleep(2)
    try:
        valor = driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr/td[1]').text
        status = driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr/td[8]').text
        
        if valor and status:
            gerenciando_canhoto(valor,status)
            time.sleep(3)
    except Exception:
        pass
    
for item in lista_canhotos:
    print('==========================================\n')
    print(f'==== Tentando encontrar o canhoto: {item}')
    findCanhoto(item)
    
print("====== FIM DA EXECUÇÃO ======")