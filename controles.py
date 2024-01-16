import os
import time
import pyautogui
from acessos import CAMINHO, ANT_CAMINHO
from main import driver


def canhoto_pendente(canhoto,valor):
    if valor == canhoto:
        print(f'{valor} encontrado')
        print(f'Movendo canhoto {valor} para a pasta CANHOTOS_PENDENTES')
        arquivo_origem = os.path.join(f'{CAMINHO}/CANHOTOS/',canhoto)
        arquivo_destino = os.path.join(f'{CAMINHO}/CANHOTOS_PENDENTES/',canhoto)
        os.rename(arquivo_origem, arquivo_destino)
        print(f"-----------{canhoto}------------- MOVIDO!")
        time.sleep(1)
        se_pendente(canhoto)

def canhoto_digitalizado(canhoto,valor):
    if valor == canhoto:
        print(f'{valor} encontrado')
        print(f'Movendo canhoto {valor} para a pasta CANHOTOS_DIGITALIZADOS')
        arquivo_origem = os.path.join(f'{CAMINHO}/CANHOTOS/',canhoto)
        arquivo_destino = os.path.join(f'{CAMINHO}/CANHOTOS_DIGITALIZADOS/',canhoto)
        os.rename(arquivo_origem, arquivo_destino)
        print(f"-----------{canhoto}------------- MOVIDO!")

        
def canhoto_rejeitado(canhoto,valor):
    if valor == canhoto:
        print(f'{valor} encontrado')
        print(f'Movendo canhoto {valor} para a pasta CANHOTOS_REJEITADOS')
        arquivo_origem = os.path.join(f'{CAMINHO}/CANHOTOS/',canhoto)
        arquivo_destino = os.path.join(f'{CAMINHO}/CANHOTOS_REJEITADOS/',canhoto)
        os.rename(arquivo_origem, arquivo_destino)
        print(f"-----------{canhoto}------------- MOVIDO!")
        time.sleep(1)
        se_pendente(canhoto)
    
    
def se_pendente(canhoto):
    driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr/td[13]/div/button').click()
    driver.find_element('xpath','/html/body/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr/td[13]/div/div/a[4]').click()
    time.sleep(3)
    pyautogui.typewrite(f'{ANT_CAMINHO}\{canhoto}')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    print(f"------------{canhoto}-- ENVIADO PARA A DANONE ---------------------")
