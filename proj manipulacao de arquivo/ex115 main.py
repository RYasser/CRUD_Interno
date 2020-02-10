# -*- coding: utf-8 -*-
from sys import exit
from time import sleep
from ex115 import consistencia, cadastro, conteudo, excluir

opc = consistencia.menu()
while True:
    if opc == 1:
        conteudo.visualizacao()
        sleep(1)
        opc = consistencia.menu()

    elif opc == 2:
        cadastro.registro()
        sleep(1)
        opc = consistencia.menu()

    elif opc == 3:
        excluir.delete()
        sleep(1)
        opc = consistencia.menu()

    elif opc == 4:
        exit()
        break

    else:
        print('\033[1;31mERRO: Opção inválida, tente novamente.\033[m')
        sleep(1)
        opc = consistencia.menu()