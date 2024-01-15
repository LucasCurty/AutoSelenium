import os
from acessos import CAMINHO

folder = os.listdir(CAMINHO)
folder_canhotos = []
for i in folder:
    canhoto = i.split('.')
    canhoto.pop()
    folder_canhotos.append(canhoto)
    