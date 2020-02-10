# -*- coding: utf-8 -*-
def delete():
    pessoas = list()

    pessoa = str(input('Informe a pessoa que deseja excluir: '))
    while pessoa.isnumeric():
        print('\033[1;31mERRO: Tipo inválido, tente novamente!\033[m')
        pessoa = str(input('Informe a pessoa que deseja excluir: '))

    arquivo = open('pessoas.txt', 'r', encoding="utf8")

    for linha in arquivo:
        linha = linha.rstrip()
        pessoas.append(linha)

    verificador = False
    for j in pessoas:
        if pessoa not in j:
            verificador = False
        else:
            verificador = True
            break
    if verificador:
        for i in pessoas:
            if pessoa in i:
                del(pessoas[pessoas.index(i)])
                print(f'{pessoa} deletado(a) com sucesso!')
            arquivo.close()

            arquivo = open('pessoas.txt', 'w', encoding="utf8")

            for linha in pessoas:
                linha = linha.rstrip()
                arquivo.write(f'{linha}\n')
    else:
        print(f'{pessoa} não está cadastrado(a)!')
