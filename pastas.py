import os
from acessos import CAMINHO

#Conferindo pastas, se nao existe o sistema cria.
# teste = []
# digitalizados = f'{CAMINHO}/CANHOTOS_DIGITALIZADOS'
# ag_aprovacao = f'{CAMINHO}/CANHOTOS_AG_APROVAÇÃO'
# nao_encontrados = f'{CAMINHO}/CANHOTOS_NAO_ENCONTRADOS'
# pendentes = f'{CAMINHO}/CANHOTOS_PENDENTES'
# rejeitados = f'{CAMINHO}/CANHOTOS_REJEITADOS'

# teste.append(digitalizados)
# teste.append(ag_aprovacao)
# teste.append(nao_encontrados)
# teste.append(pendentes)
# teste.append(rejeitados)

# for i in teste:
    
#     if os.path.exists(i) == False:
#         os.mkdir(i)
#         print(i)

folder = os.listdir(f'{CAMINHO}/CANHOTOS')
folder_canhotos = []
for i in folder:
    os.rename(f'{CAMINHO}/CANHOTOS/{i}',f'{CAMINHO}/CANHOTOS/{i}.png')
    canhoto = i.split('.')
    canhoto.pop()
    folder_canhotos.append(canhoto)
    
    print(folder_canhotos)
    