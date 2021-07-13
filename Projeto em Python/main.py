#PROGRAMA TESTE PARA CONTRATAÇÃO ESTAGIO QWA SOLUCOES
#CADASTRO DE CLIENTES XPTO - TRAINEES
#GITHUB/FELIPERDEV

import os
import funcoes

clear = lambda: os.system('cls')
etapa = 1

def menuInicial (etapa):
    usuariosCadastrados = funcoes.contarCampos()
    valorUsuariosTemporarios = len(funcoes.usuariosTemporarios)

    if(etapa == 1):
        clear()
        print(" Bem vindo ao programa de teste XPTO, para a QWA Soluções")
        print(" Desenvolvido por: Felipe Rosario Dos Santos - @FelipeRDEV\n")
        print(" Vagas disponíveis: ",''.join(funcoes.nomeVagas),"\n")
        print(" Máximo de candidatos por vaga: ", funcoes.maximoDeVagas)
        print(" Valor restante de cadastros no banco de dados: ", funcoes.maximoDeCadastros - usuariosCadastrados)
        print(" Valor máximo de cadastros restantes da lista atual: ", funcoes.maximoDeCadastros - valorUsuariosTemporarios, "\n")
        print(" Por favor, selecione uma das opções abaixo \n")
        print(" 1 - Cadastrar um usuário em uma vaga")
        print(" 2 - Revisar/Exibir a lista atual de usuários temporarios")
        print(" 3 - Limpar as lista temporaria")
        print(" 4 - Confirmar e salvar todos os usuários")
        print(" 5 - Consultar o banco de dados")
        print(" 6 - Apagar todos os registros do banco de dados")
        print(" 7 - Sair\n")

    if(etapa == 2):

        print('\n')
        print(" Máximo de candidatos por vaga: ", funcoes.maximoDeVagas)
        print(" Valor restante de cadastros no banco de dados: ", funcoes.maximoDeCadastros - usuariosCadastrados)
        print(" Valor máximo de cadastros restantes da lista atual: ", funcoes.maximoDeCadastros - valorUsuariosTemporarios, "\n")
        print(" Por favor, selecione uma das opções abaixo \n")
        print(" 1 - Cadastrar um usuário em uma vaga")
        print(" 2 - Revisar/Exibir a lista atual de usuários temporarios")
        print(" 3 - Limpar as lista temporaria")
        print(" 4 - Confirmar e salvar todos os usuários")
        print(" 5 - Consultar o banco de dados")
        print(" 6 - Apagar todos os registros do banco de dados")
        print(" 7 - Sair\n")

    escolha = (input(""))
    checkEscolha = escolha.isnumeric()
    clear()

    while (checkEscolha != True):
        clear()
        print('\n')
        print(" Máximo de candidatos por vaga: ", funcoes.maximoDeVagas)
        print(" Valor restante de cadastros no banco de dados: ", funcoes.maximoDeCadastros - usuariosCadastrados)
        print(" Valor máximo de cadastros restantes da lista atual: ", funcoes.maximoDeCadastros - valorUsuariosTemporarios, "\n")
        print(" Por favor, selecione uma das opções abaixo \n")
        print(" 1 - Cadastrar um usuário em uma vaga")
        print(" 2 - Revisar/Exibir a lista atual de usuários temporarios")
        print(" 3 - Limpar as lista temporaria")
        print(" 4 - Confirmar e salvar todos os usuários")
        print(" 5 - Consultar o banco de dados")
        print(" 6 - Apagar todos os registros do banco de dados")
        print(" 7 - Sair\n")
        escolha = (input(" Por favor, utilize somente números na escolha da opção desejada:\n "))
        checkEscolha = escolha.isnumeric()


    while (int(escolha) <1 or int(escolha) >8):
        clear()
        print('\n')
        print(" Máximo de candidatos por vaga: ", funcoes.maximoDeVagas)
        print(" Valor restante de cadastros no banco de dados: ", funcoes.maximoDeCadastros - usuariosCadastrados)
        print(" Valor máximo de cadastros restantes da lista atual: ", funcoes.maximoDeCadastros - valorUsuariosTemporarios, "\n")
        print(" Por favor, selecione uma das opções abaixo \n")
        print(" 1 - Cadastrar um usuário em uma vaga")
        print(" 2 - Revisar/Exibir a lista atual de usuários temporarios")
        print(" 3 - Limpar as lista temporaria")
        print(" 4 - Confirmar e salvar todos os usuários")
        print(" 5 - Consultar o banco de dados")
        print(" 6 - Apagar todos os registros do banco de dados")
        print(" 7 - Sair\n")
        escolha = (input(" Opção Inválida, por favor, utilize somente números de 1 a 7:\n "))
        checkEscolha = escolha.isnumeric()

        while(checkEscolha != True):
            clear()
            print(" Máximo de candidatos por vaga: ", funcoes.maximoDeVagas)
            print(" Valor restante de cadastros no banco de dados: ", funcoes.maximoDeCadastros - usuariosCadastrados)
            print(" Valor máximo de cadastros restantes da lista atual: ", funcoes.maximoDeCadastros - valorUsuariosTemporarios, "\n")
            print(" 1 - Cadastrar um usuário em uma vaga")
            print(" 2 - Revisar/Exibir a lista atual de usuários temporarios")
            print(" 3 - Limpar as lista temporaria")
            print(" 4 - Confirmar e salvar todos os usuários")
            print(" 5 - Consultar o banco de dados")
            print(" 6 - Apagar todos os registros do banco de dados")
            print(" 7 - Sair\n")
            escolha = (input(" Opção Inválida, por favor, utilize somente números de 1 a 3:\n "))
            checkEscolha = escolha.isnumeric()

    escolha = (int(escolha))

    if (escolha == 1):
        dadosCorretos = funcoes.prosseguirCadastro()
        if (dadosCorretos != True):
            menuInicial(2)

    elif (escolha == 2):
        clear()
        funcoes.buscaTemporarios()
        menuInicial(2)

    elif (escolha == 3):
        clear()
        listaLimpa = funcoes.limparListaTemp(funcoes.usuariosTemporarios)
        if (listaLimpa == True):
            clear()
            print (" A lista temporaria foi limpa com sucesso!\n")
        else:
            print (" A lista temporaria não pode ser limpa!\n")
        menuInicial(2)

    elif (escolha == 4):
        clear()
        funcoes.cadastrarBanco()
        print("\n")

    elif (escolha == 5):
        clear()
        funcoes.buscaBanco()

    elif (escolha == 6):
        clear()
        funcoes.apagarBanco()

    elif (escolha == 7):
        print(" Até logo!\n")
        exit(0)

    menuInicial(2)

menuInicial(1)

