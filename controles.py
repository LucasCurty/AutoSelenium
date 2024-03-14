import os
from acessos import CAMINHO

def canhoto_pendente(canhoto,valor):
    if valor == canhoto:
        print(f'Movendo canhoto {valor} para a pasta CANHOTOS_PENDENTES')
        arquivo_origem = os.path.join(f'{CAMINHO}/CANHOTOS/',canhoto)
        arquivo_destino = os.path.join(f'{CAMINHO}/CANHOTOS_PENDENTES/',canhoto)
        os.rename(arquivo_origem, arquivo_destino)
        print(f"-----------{canhoto}------------- MOVIDO!")

def canhoto_digitalizado(canhoto,valor):
    if valor == canhoto:
        print(f'Movendo canhoto {valor} para a pasta CANHOTOS_DIGITALIZADOS')
        arquivo_origem = os.path.join(f'{CAMINHO}/CANHOTOS/',canhoto)
        arquivo_destino = os.path.join(f'{CAMINHO}/CANHOTOS_DIGITALIZADOS/',canhoto)
        os.rename(arquivo_origem, arquivo_destino)
        print(f"-----------{canhoto}------------- MOVIDO!")

        
def canhoto_rejeitado(canhoto,valor):
    if valor == canhoto:
        print(f'Movendo canhoto {valor} para a pasta CANHOTOS_REJEITADOS')
        arquivo_origem = os.path.join(f'{CAMINHO}/CANHOTOS/',canhoto)
        arquivo_destino = os.path.join(f'{CAMINHO}/CANHOTOS_REJEITADOS/',canhoto)
        os.rename(arquivo_origem, arquivo_destino)
        print(f"-----------{canhoto}------------- MOVIDO!")

def canhoto_Aguardando_Aprovacao(canhoto,valor):
    if valor == canhoto:
        print(f'Movendo canhoto {valor} para a pasta CANHOTOS_AG_APROVAÇÃO')
        arquivo_origem = os.path.join(f'{CAMINHO}/CANHOTOS/',canhoto)
        arquivo_destino = os.path.join(f'{CAMINHO}/CANHOTOS_AG_APROVAÇÃO/',canhoto)
        os.rename(arquivo_origem, arquivo_destino)
        print(f"-----------{canhoto}------------- MOVIDO!")
