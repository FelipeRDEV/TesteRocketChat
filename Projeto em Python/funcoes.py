#PROGRAMA TESTE PARA CONTRATAÇÃO ESTAGIO QWA SOLUCOES
#CADASTRO DE CLIENTES XPTO - TRAINEES
#GITHUB/FELIPERDEV

import datetime
import classes
import os
import sqlite

usuariosTemporarios = []

'''usuariosTemporarios = [('Candidatos', 'Teste', '12345678912', 242000, 21, 'Sim', 'Analista'),('Ficticio', 'Ficjhonson', '12345678999', 942002, 11, 'Não', 'Analista')
             ,('Bruninho', 'Midias', '12432123433', 642001, 14, 'Não', 'Analista'),('Gabriel', 'Bebezinho', '12432123434', 342020, 18, 'Sim', 'Rh')
             ,('Renan', 'Fonseca', '12432123435', 941998, 29, 'Sim', 'Analista'),('Luana', 'Policheck', '12432123436', 352013, 22, 'Sim', 'Administração')
             ,('Luiza', 'Alves', '12432123436', 542001, 11, 'Não', 'Administração'),('Pão', 'Francês', '12432123438', 942002, 11, 'Não', 'Administração')
             ,('Beatriz', 'Silva', '12432123437', 942002, 11, 'Não', 'Desenvolvedor')]'''

#tempUser para testes, incluirá 9 candidatos à uma lista de inserção, desta lista, apenas 7 usuarios serão inseridos, pois 1 dará erro de CPF ja existente \
# e outro dará que a profissão Analista ja atingiu seu limite de 3 pessoas para esta vaga

clear = lambda: os.system('cls')
nomeVagas = ["Desenvolvedor (Dev) ", "Analista ", "RH ", "Manutenção ", "Administração "]
maximoDeVagas = 3
maximoDeCadastros = 10
debug = 0

def perguntarNome():
    entradaNome = input(" Primeiro Nome: ")
    nomeValido = entradaNome.isalpha()

    if (entradaNome.lower() == 'sair'):
        clear()
        return False

    while (nomeValido != True):
        print(" Por favor, utilize somente letras para inserir um nome.\n")
        entradaNome = input(" Digite novamente o primeiro nome do cliente a ser cadastrado, ou digite Sair: ")
        nomeValido = entradaNome.isalpha()

    return entradaNome.capitalize()

def perguntarSobrenome ():
    entradaSobrenome = input(" Sobrenome: ")

    if all(x.isalpha() or x.isspace() for x in entradaSobrenome):
        sobrenomeValido = True
    else:
        sobrenomeValido = False

    if (entradaSobrenome.lower() == 'sair'):
        clear()
        return False

    while (sobrenomeValido != True):
        print(" Por favor, utilize somente letras para inserir um sobrenome.")
        entradaSobrenome = input(" Digite novamente o sobrenome do cliente a ser cadastrado, ou digite Sair: ")
        sobrenomeValido = entradaSobrenome.isalpha() or entradaSobrenome.isspace()

    return entradaSobrenome.capitalize()

def perguntarCpf():
    entradaCpf = input(" CPF: ")
    cpfNumerico = entradaCpf.isnumeric()
    cpfTamanho = len(entradaCpf)

    if (entradaCpf.lower() == 'sair'):
        clear()
        return False

    while (cpfNumerico != True):
        print(" CPF deve conter apenas números.")
        entradaCpf = input(" Digite novamente o CPF do cliente a ser cadastrado, ou digite Sair: ")
        cpfNumerico = entradaCpf.isnumeric()
        if (entradaCpf.lower() == 'sair'):
            clear()
            return False

    while (cpfTamanho != 11):
        print(" CPF deve conter 11 digitos.")
        entradaCpf = input(" Digite novamente o CPF do cliente a ser cadastrado, ou digite Sair: ")
        cpfTamanho = len(entradaCpf)
        if (entradaCpf.lower() == 'sair'):
            clear()
            return False

    if (cpfNumerico == True and cpfTamanho == 11):
        return entradaCpf

def encontrarCpf(numeroCpf):

    cpfEncontrado =sqlite.lerCpfs(numeroCpf)

    return cpfEncontrado

def encontrarCpfTemp (numeroCpf):

    i = 0
    for registro in usuariosTemporarios:
        if numeroCpf in registro:
            i += 1
            break
    else:
        return False

    return True

def perguntarDatanasc ():
    checagemAno = datetime.date.today()
    # Checa o ano atual,
    anoAtual = int(checagemAno.strftime("%Y"))
    #Converte-o em Inteiro para que possa ser usado como parametro

    entradaDia = input(" Dia de nascimento: ")
    entradaMes = input(" Mês de nascimento (Número): ")
    entradaAno = input(" Ano de nascimento: ")

    if (entradaDia.lower() == "sair"):
        clear()
        return False

    if (entradaMes.lower() == "sair"):
        clear()
        return False

    if (entradaAno.lower() == "sair"):
        clear()
        return False

    dataValida = entradaDia.isnumeric() and entradaMes.isnumeric() and entradaAno.isnumeric()

    while (dataValida != True):
        print(" Por favor, utilize apenas números para inserir uma data de nascimento, digite Sair para encerrar.")

        entradaDia = input(" Dia de nascimento: ")
        entradaMes = input(" Mês de nascimento (Numero): ")
        entradaAno = input(" Ano de nascimento: ")
        dataValida = entradaDia.isnumeric() and entradaMes.isnumeric() and entradaAno.isnumeric()

    diaInt = int(entradaDia)
    mesInt = int(entradaMes)
    anoInt = int(entradaAno)

    while (diaInt > 31 or diaInt < 1):
        checarDia = input(" Dia inválido, o dia só pode valer entre 1 e 31, digite-o novamente ou digite Sair: ")
        if (checarDia.lower() == "sair"):
            clear()
            return False
        diaValido = checarDia.isnumeric()
        while (diaValido != True):
            checarDia = input(" Dia inválido, o dia só pode valer entre 1 e 31, digite-o novamente ou digite Sair: ")
            if(checarDia.lower() == "sair"):
                clear()
                return False
            diaValido = checarDia.isnumeric()
        diaInt = int(checarDia)
    #Checa se o dia digitado possui valor entre 1 e 31, excluindo a necessidade de validar se foram digitados
    #dois digitos.

    while (mesInt > 12 or mesInt < 1):
        checarMes = input(" Mês inválido, o mês só pode valer entre 1 e 12, digite-o novamente ou digite Sair: ")
        if(checarMes.lower() == "sair"):
            clear()
            return False
        mesValido = checarMes.isnumeric()
        while (mesValido != True):
            checarMes = input(" Mês inválido, o mês só pode valer entre 1 e 12, digite-o novamente ou digite Sair: ")
            if (checarMes.lower() == "sair"):
                clear()
                return False
            mesValido = checarMes.isnumeric()
        mesInt = int(checarMes)
    #Checa se o mes digitado possui valor entre 1 e 12, da mesma forma da validação dos dias.

    while (anoInt > anoAtual or anoInt < 1900):
        checarAno = input(" Ano inválido, o ano só pode valer entre 1900 e o ano atual, digite-o novamente ou digite Sair: ")
        if (checarAno.lower() == "sair"):
            clear()
            return False
        anoValido = checarAno.isnumeric()
        while (anoValido != True):
            checarAno = input(" Ano inválido, o ano só pode valer entre 1900 e o ano atual, digite-o novamente ou digite Sair: ")
            if (checarAno.lower() == "sair"):
                clear()
                return False
            anoValido = checarAno.isnumeric()
        anoInt = int(checarAno)
    #Checa se o ano digitado possui valor entre 1900 e o ano atual, seguindo a logica da media de vida de um ser humano.

    dataCompleta = str(diaInt) + str(mesInt) + str(anoInt)

    return anoInt, mesInt, diaInt, dataCompleta

def perguntarVaga ():
    print('\n')
    print(" Vagas disponíveis: ", ''.join(nomeVagas),"\n")
    entradaVaga = input(" Digite a vaga do cliente a ser cadastrado: ")
    checarVagaAlpha = entradaVaga.isalpha()

    if (entradaVaga.lower() == "sair"):
        clear()
        return False

    while (checarVagaAlpha != True):
        print(" Escolha da vaga deve conter apenas letras!\n")
        print(" Vagas disponíveis: ", ''.join(nomeVagas))
        entradaVaga = input(" Escreva novamente a vaga do cliente a ser cadastrado ou digite Sair: ")
        if (entradaVaga.lower() == "sair"):
            clear()
            return False
        checarVagaAlpha= entradaVaga.isalpha()


    while (entradaVaga.lower() != "desenvolvedor" and  entradaVaga.lower() != "dev" and entradaVaga.lower() != "analista" and entradaVaga.lower() \
           and entradaVaga.lower() != "rh" and entradaVaga.lower() != "manutenção" and entradaVaga.lower() != "manutencao" \
           and entradaVaga.lower() != "manutençao" and entradaVaga.lower() != "administração" and \
           entradaVaga.lower() != "administracao" and entradaVaga.lower() != "administraçao" and entradaVaga.lower() != "admin" \
            and entradaVaga.lower() != "adm"):

        print(" Vagas disponíveis: ", ''.join(nomeVagas),"\n")
        entradaVaga = input(" Opção Inválida, escreva novamente a vaga do cliente a ser cadastrado ou digite Sair: ")
        if (entradaVaga.lower() == "sair"):
            clear()
            return False


    return entradaVaga.capitalize()


def calcularIdade(dataNascimento):

    hoje = datetime.date.today()
    idadeFinal = hoje.year - dataNascimento.year - ((hoje.month, hoje.day) < (dataNascimento.month, dataNascimento.day))

    return idadeFinal

def definirMaioridade (idade):
    if (idade < 18):
        return False
    else:
        return True

def contarCampos ():
    contagem = sqlite.procurarEntrada()
    if (contagem == False):
        return 0
    else:
        return contagem[0]

def cadastrarTemporarios (nome, sobrenome, cpf, datanasc, idade, maioridade, vaga):

    quantiaTemporarios = len(usuariosTemporarios)
    entrada = (nome, sobrenome, cpf, datanasc, idade, maioridade, vaga)

    if (debug == 1):
        for x in usuariosTemporarios:
            print("ATUAL TEMP USERS: ", x)
        print("TEMP USER INTEIRO: ", usuariosTemporarios)

    if (quantiaTemporarios < 10):
        usuariosTemporarios.append(entrada)
        return True
    else:
        return False

def limparListaTemp (usuariosTemporarios):

    usuariosTempVazio, usuariosTemporarios[:] = usuariosTemporarios[:], []

    if (usuariosTempVazio == []):
        return True
    else:
        return False


def cadastrarBanco():
    quantiaTemporarios = len(usuariosTemporarios)
    naoInseridos = 0

    if (debug == 1):
        print ("TAMANHO TEMP USERS: ", quantiaTemporarios)

    if (usuariosTemporarios == []):
        print(" Lista de usuários temporarios não pode estar vazia, nenhum usuário foi cadastrado.\n")
        return False

    for usuario in usuariosTemporarios:
        cpfProtecao = encontrarCpf(usuario[2])

        if (debug == 1):
            print("CPF NO TEMPUSER :", usuario[2])
            print("VAGA NO TEMPUSER: ", usuario[6])
            print("CPF PROTECAO: ", cpfProtecao)

        if(cpfProtecao != True):
            retornoEntrada = sqlite.registrarDados(usuario)
            if (retornoEntrada == False):
                print(" Erro ao cadastrar, quantidade máxima de registros no banco foi atingida!\n")
        else:
            naoInseridos = 1
            print(" Não foi possível inserir o usuário ",usuario[0], usuario[1], "de CPF: ", usuario[2], "pois este CPF já foi cadastrado.\n")

    if (usuariosTemporarios != []):
        if (naoInseridos != 1):
            print(" Dados enviados para o banco de dados, por favor, verifique utilizando a opção 4.\n")
        else:
            print(" Dados inseridos no banco de dados, exceto os quais apontam erro, por favor, verifique utilizando a opção 4.\n")


def buscaTemporarios():
    print("                                               USUÁRIOS TEMPORARIOS                                                  \n")
    print("|    NOME    |     SOBRENOME       |       CPF       |      NASCIMENTO      |    IDADE    | MAIOR DE 18  |   VAGA   |\n")
    if (usuariosTemporarios == []):
        print(" Nenhum usuário temporário foi cadastrado ainda.")
    else:
        for x in usuariosTemporarios:
            print(x, "\n")

    print(" Número de registros na lista temporária atualmente: ", len(usuariosTemporarios))

def buscaBanco():
    print("                                                  BANCO DE DADOS                                                     \n")
    print("|    NOME    |     SOBRENOME       |       CPF       |      NASCIMENTO      |    IDADE    | MAIOR DE 18  |   VAGA   |\n")

    retornoEntrada = sqlite.procurarEntrada()
    registros = 0

    if (retornoEntrada == False):
        print(" Nenhum usuário cadastrado no banco até o momento.")
    else:
        retornoArray = retornoEntrada[1]
        for x in range(retornoEntrada[0]):
            registros = registros + 1
            print(retornoArray[x], "\n")

    print(" Número de registros no banco de dados atualmente: ", registros)

def apagarBanco ():
    bancoApagado = sqlite.apagarRegistros()
    if (bancoApagado == True):
        print(" Todos os registros do banco foram apagados com sucesso!")
    else:
        print(" Houve um erro ao apagar os registros do banco, contate um administrador.")

def prosseguirCadastro():
    clear()

    print("\n")
    print("                                                  CADASTRO DE USUÁRIO                                                  \n")
    print(" Digite sair a qualquer momento para voltar ao menu inicial. \n")

    classes.Pessoa.nome = perguntarNome()

    if (classes.Pessoa.nome == False):
        clear()
        return False

    classes.Pessoa.sobrenome = perguntarSobrenome()

    if (classes.Pessoa.sobrenome == False):
        clear()
        return False

    classes.Pessoa.cpf = perguntarCpf()

    if (classes.Pessoa.cpf == False):
        clear()
        return False

    classes.Pessoa.datanasc = perguntarDatanasc()

    if (classes.Pessoa.datanasc == False):
        clear()
        return False

    classes.objetoData.ano = classes.Pessoa.datanasc[0]
    classes.objetoData.mes = classes.Pessoa.datanasc[1]
    classes.objetoData.dia = classes.Pessoa.datanasc[2]

    calcIdade = (calcularIdade(datetime.date(classes.objetoData.ano,classes.objetoData.mes,classes.objetoData.dia)))
    idade = calcIdade

    if (idade == -1):
        idade = 0

    #Em caso de idades menores que um ano

    maioridade = definirMaioridade(idade)

    if (maioridade == True):
        maioridade = "Sim"
    else:
        maioridade = "Não"

    vagaSelecionada = perguntarVaga()

    if (vagaSelecionada == False):
        clear()
        return False

    dataCompleta = classes.Pessoa.datanasc[3]
    envioDataNascimento = int(dataCompleta)

    clear()
    print("\n")
    print(" Por favor, confirme se os dados a seguir estão corretos: \n")
    print(" Nome: ", classes.Pessoa.nome)
    print(" Sobrenome: ", classes.Pessoa.sobrenome)
    print(" CPF: ", classes.Pessoa.cpf)
    print(" Data de Nascimento: ", classes.Pessoa.datanasc[2], classes.Pessoa.datanasc[1], classes.Pessoa.datanasc[0])
    print(" Idade: ", idade)
    print(" Maior de 18: ", maioridade)
    print(" Vaga selecionada: ", vagaSelecionada, "\n")

    dadosCorretos = input(" Os dados estão dados corretos? Digite Sim, Não ou Sair: ")

    while (dadosCorretos.lower() != "sim" and dadosCorretos.lower() != "s" and dadosCorretos.lower() != "não" \
               and dadosCorretos != "nao" and dadosCorretos.lower() != "n" and dadosCorretos.lower() != "sair"):

        clear()
        print("\n")
        print(" Por favor, confirme se os dados a seguir estão corretos: \n")
        print(" Nome: ", classes.Pessoa.nome)
        print(" Sobrenome: ", classes.Pessoa.sobrenome)
        print(" CPF: ", classes.Pessoa.cpf)
        print(" Data de Nascimento: ", classes.Pessoa.datanasc[2], classes.Pessoa.datanasc[1],
              classes.Pessoa.datanasc[0])
        print(" Idade: ", idade)
        print(" Maior de 18: ", maioridade)
        print(" Vaga selecionada: ", vagaSelecionada, "\n")
        dadosCorretos = input(" Entrada inválida, Os dados estão dados corretos? \n Digite Sim, Não ou Sair: ")

    if (dadosCorretos.lower() == "sim" or dadosCorretos.lower() == "s"):
        checagemCpfTemp = encontrarCpfTemp(classes.Pessoa.cpf)

        if (checagemCpfTemp == False):
            sucessoCadastro = cadastrarTemporarios(classes.Pessoa.nome, classes.Pessoa.sobrenome, classes.Pessoa.cpf, envioDataNascimento, idade, maioridade, vagaSelecionada)

            if (sucessoCadastro == True):
                clear()
                print("\n")
                print(" Adcionado à lista temporária de cadastro com sucesso.\n")
                return True
            else:
                clear()
                print(" Usuário não adcionado à lista de cadastros temporários, numero máximo de registros alcançado!")
                return False

        else:
            if(checagemCpfTemp != False):
                clear()
                print(" Erro ao cadastrar, este CPF já foi inserido na fila temporária!\n")
            else:
                clear()
                print(" Erro ao adicionar à fila de cadastros temporários.")
            return False

    elif (dadosCorretos.lower() == "não" or dadosCorretos.lower() == "n" or dadosCorretos.lower() == "nao"):
        clear()
        print(" Ok, insira novamente seus dados\n")
        return False

    elif (dadosCorretos.lower() == "sair"):
        clear()
        return False



