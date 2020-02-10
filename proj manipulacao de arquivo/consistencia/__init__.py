# -*- coding: utf-8 -*-
def lin():
    print('-' * 46)
def menu():
    lin()
    print('               MENU PRINCIPAL')
    lin()
    print('\033[1;32m'
          '1 - \033[m\033[1;34mVer pessoas cadastradas\n\033[1;32m'
          '2 - \033[m\033[1;34mCadastrar nova Pessoa\n\033[1;32m'
          '3 - \033[m\033[1;34mExcluir Pessoas\033[m\n\033[1;32m'
          '4 - \033[m\033[1;34mSair do Sitema\033[m')
    lin()
    while True:
        try:
            opcao = int(input('\033[1;32mSua Opção: \033[m'))
            lin()
        except:
            print('\033[1;31mERRO: Valor inválido, tente novamente!\033[m')
        else:
            break
    return opcao