import os
from acessos import CAMINHO

#Conferindo pastas, se nao existe o sistema cria.

def create_folders():
    pastas = [
        f'{CAMINHO}CANHOTOS_DIGITALIZADO',
        f'{CAMINHO}CANHOTOS_AG. APROVAÇÃO',
        f'{CAMINHO}CANHOTOS_NAO ENCONTRADOS',
        f'{CAMINHO}CANHOTOS_PENDENTE',
        f'{CAMINHO}CANHOTOS_REJEITADO'
    ]

    for i in pastas:
        if os.path.exists(i) == False:
            os.mkdir(i)
            print("====Pasta criada com sucesso! ", i)
        else:
            print(f"===Caminho {i} encontrado!")

def rename_arquivos():
    folder = os.listdir(f'{CAMINHO}CANHOTOS')
    folder_canhotos = []
    for i in folder:
        canhoto = i.split('.')
        canhoto.pop()
        novo_canhoto = canhoto[0]
        os.rename(f'{CAMINHO}CANHOTOS/{i}',f'{CAMINHO}CANHOTOS/{novo_canhoto}.png')
        folder_canhotos.append(novo_canhoto)        
    return folder_canhotos
        
