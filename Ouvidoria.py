from operacoesbd import *

conexao = criarConexao('localhost', 'root', 'LeonardoADS26', 'Ouvidoria')


def registrar_reclamacao(conexao):
    motivo_reclamacao = input('Digite o motivo da reclamação: ')
    reclamacao = input('Explique o seu problema:')

    categoria = "Reclamação"
    consulta = 'insert into Ouvidoria (tipo, descricao, categoria) values (%s,%s,%s);'
    dados = [motivo_reclamacao, reclamacao, categoria]
    cod_reclamacao = insertNoBancoDados(conexao, consulta, dados)

    print('Reclamação Adicionada com sucesso, o código da sua reclamação é:', cod_reclamacao)

def listar_reclamacoes(conexao):

    consulta = "select * from Ouvidoria where categoria = 'Reclamação';"
    reclamacoes = listarBancoDados(conexao, consulta)

    if len(reclamacoes) > 0:

        print('Lista de Reclamações')
        
        for item in reclamacoes:
            print('\n Título:', item[1], '\n Descrição:', item[2], '\n Código:', item[0])

    else:
        print('Não existem reclamações a serem exibidas')

def pesquisar_reclamacao(conexao):
    try:
        codigo = int(input("Digite o código da reclamação: "))
    except ValueError:
        print('Erro: Digite apenas números!')
        return

    consulta = 'select * from Ouvidoria where codigo = %s and categoria = %s;'
    dados = [codigo, "Reclamação"]

    reclamacoes = listarBancoDados(conexao, consulta, dados)

    if len(reclamacoes) > 0:

        print('Reclamação Encontrada')
        for item in reclamacoes:
            print('\n Título:', item[1], '\n Descrição:', item[2], '\n Código:', item[0])
    else:
        print('Reclamação não encontrada')

def atualizar_reclamacao(conexao):
    try:
        cod_reclamacao = int(input('Digite o código da reclamação que deseja atualizar: '))
    except ValueError:
        print('Erro: Digite apenas números!')
        return
    
    nova_descricao = input('Digite a nova descrição da reclamação: ')

    consulta = "update Ouvidoria set descricao = %s where codigo = %s and categoria = 'Reclamação';"
    dados = [nova_descricao, cod_reclamacao]

    att = atualizarBancoDados(conexao, consulta, dados)


    if att > 0:
        print('Reclamação atualizada com sucesso!')

    else:
        print('Código informado é invalido')

def remover_reclamacao(conexao):
    try:
        cod_reclamacao = int(input('Digite o código da reclamação que deseja remover: '))
    except ValueError:
        print('Erro: Digite apenas números!')
        return

    consulta = "delete from Ouvidoria where codigo = %s and categoria = 'Reclamação';"
    dados = [cod_reclamacao]

    removidos = excluirBancoDados(conexao, consulta, dados)

    if removidos > 0:
        print('Reclamação removida com sucesso!')

    else:
        print('Código informado é invalido')




    