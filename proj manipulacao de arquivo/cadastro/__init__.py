# -*- coding: utf-8 -*-
def registro():
    while True:
        nome = str(input('Nome: ')).strip()
        if nome.isalpha():
            break
    try:
        idade = int(input(f'Idade do {nome}: '))
    except:
        print('\033[1;31mERRO: Valor inválido, tente novamente!\033[m')
    else:

        arquivo = open('pessoas.txt', 'a', encoding='utf8')

        arquivo.write(f'{nome}')
        arquivo.write(' '*(34-len(nome)))
        arquivo.write(f'{idade} anos\n')
        print(f'{nome} cadastrado com sucesso!')
        arquivo.close()
