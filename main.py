from selenium import webdriver
from acessos import LOGIN,SENHA,URL,CAMINHO
from pastas import folder_canhotos,folder
import time
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
time.sleep(3)
driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[4]/div/div/input').clear()
time.sleep(3)

def canhoto_pendente(canhoto,valor):
    if f'{valor}.png' == canhoto:
        print(f'{valor} encontrado')
        print(f'Movendo canhoto {valor} para a pasta CANHOTOS_PENDENTES')
        os.rename(f'{CAMINHO}\\{canhoto}', f'H:\\Meu Drive\\CANHOTOS_PENDENTES\\{canhoto}')
        print(f"{canhoto} movido")
                    
def findCanhoto(canhoto):
    driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div/input').clear()
    driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(canhoto)
    driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[1]/div/div/div/div/div[3]/button[4]').click()
    time.sleep(1.5)
    valor = driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr/td[1]').text
    status = driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr/td[8]').text
    if valor:
        if status == "Entregue":
            print(f"O Canhoto {valor} encontrase com o status {status}")
        if status == "Pendente":
            print(f"O Canhoto {valor} encontrase com o status {status}")
            for canhoto in folder:   
                canhoto_pendente(canhoto,valor)

        if status == "Rejeitado":
            print(f"O Canhoto {valor.text} encontrase com o status {status.text}")
            print('REJEITADO TENTE NOVAMENTE')
        time.sleep(3)
    if not valor:
        print(f"Canhoto: {valor.text} NAO ENCONTRADO")
        pass

for item in folder_canhotos:
    print(f'Tentando encontrar o canhoto: {item}')
    findCanhoto(item)
    
print("FIM DA EXECUÇÃO")