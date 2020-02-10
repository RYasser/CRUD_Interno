# -*- coding: utf-8 -*-
from ex115 import  consistencia
def visualizacao():
    arquivo = open('pessoas.txt', 'r', encoding="utf8")
    print('             PESSOAS CADASTRADAS')
    consistencia.lin()
    for linha in arquivo:
        linha = linha.rstrip()
        print(linha)