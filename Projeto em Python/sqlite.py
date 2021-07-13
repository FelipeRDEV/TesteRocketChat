#PROGRAMA TESTE PARA CONTRATAÇÃO ESTAGIO QWA SOLUCOES
#CADASTRO DE CLIENTES XPTO - TRAINEES
#GITHUB/FELIPERDEV

import sqlite3
debug = 0
connection = sqlite3.connect('xpto.db')
c = connection.cursor()


# SQL

def criar_tabela():
    c.execute('CREATE TABLE IF NOT EXISTS usuarios (nome text, sobrenome text, cpf integer, datanasc integer, idade integer, maior text, vaga text)')

criar_tabela()


def registrarDados(dadosProntos):
    contagemRegistros = c.execute('SELECT COUNT(*) FROM usuarios')
    registros = contagemRegistros.fetchone()[0]

    if (debug == 1):
        print("registros contados: ", registros)

    contagemVagas = c.execute('SELECT COUNT(*) FROM usuarios WHERE vaga =?', [dadosProntos[6]])
    vagasRegistradas = contagemVagas.fetchone()[0]

    if (debug == 1):
        print("Vagas registradas: ", vagasRegistradas)


    if (registros < 10):
        if (vagasRegistradas < 3):
            c.execute("INSERT INTO usuarios VALUES (?,?,?,?,?,?,?) ", dadosProntos)
            connection.commit()
            return True
        else:
            print("Numero maximo de registros para ", [dadosProntos[6]], "foi atingido!\n")
    else:
        return False


    if (debug == 1):
        print("contagemVagas: ", vagasRegistradas)

def lerCpfs(cpf):
    selecao = c.execute('SELECT EXISTS(SELECT 1 FROM usuarios WHERE cpf = ?)', [cpf])
    encontrados = selecao.fetchone()[0]
    if encontrados == 1:
        return True
    else:
        return False

def procurarEntrada():

    listaCampos =[]

    with connection:
        campos = 0
        c.execute("SELECT * FROM usuarios")
        fetched = c.fetchall()
        if(fetched != []):
            for x in fetched:
                campos = campos + 1
                listaCampos.append(x)
        else:
            return False

    return campos, listaCampos

def apagarRegistros ():

    c.execute('DELETE from usuarios')
    resultadoApagar = c.fetchall()

    if (resultadoApagar == []):
        return True
    else:
        return False