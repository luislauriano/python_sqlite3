from interface import titulo,menu
from dmlBanco import inserir,atualizar,excluir,getPessoa
from time import sleep

while True:
    titulo()
    menu()
    opcao = input('opcao: ')

    if opcao == 1:
         nome = input('Digite seu Nome: ')
         idade = int(input('Digite sua idade: '))
         cpf = input('Digite seu cpf: ')
         inserir(nome, idade, cpf)
         print('Cadastrado com Sucesso')