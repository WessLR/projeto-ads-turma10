from operacoesbd import *

conexao = criarConexao('localhost', 'root', 'LeonardoADS26', 'Ouvidoria')

def pedir_codigo(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Erro: Digite apenas números! Tente novamente.')

def exibir_itens(itens):
    for i, item in enumerate(itens, start=1):
        print(f'\n [{i}] Título: {item[1]}\n     Descrição: {item[2]}\n     Código: {item[0]}')

def registrar_reclamacao(conexao):
    motivo = input('Digite o motivo da reclamação: ')
    descricao = input('Explique o seu problema: ')

    categoria = "Reclamação"
    consulta = 'insert into Ouvidoria (tipo, descricao, categoria) values (%s,%s,%s);'
    dados = [motivo, descricao, categoria]
    cod_reclamacao = insertNoBancoDados(conexao, consulta, dados)

    print('Reclamação Adicionada com sucesso, o código da sua reclamação é:', cod_reclamacao)

def listar_reclamacoes(conexao):

    consulta = "select * from Ouvidoria where categoria = 'Reclamação';"
    reclamacoes = listarBancoDados(conexao, consulta)

    if reclamacoes:

        print('Lista de Reclamações')
        exibir_itens(reclamacoes)
    
    else:
        print('Não existem reclamações a serem exibidas')

def pesquisar_reclamacao(conexao):
    codigo = pedir_codigo('Digite o código da reclamação que deseja pesquisar: ')

    consulta = 'select * from Ouvidoria where codigo = %s and categoria = %s;'
    dados = [codigo, "Reclamação"]

    reclamacoes = listarBancoDados(conexao, consulta, dados)

    if reclamacoes:
        print('Reclamação Encontrada')
        exibir_itens(reclamacoes)
    else:
        print('Reclamação não encontrada')

def atualizar_reclamacao(conexao):

    codigo = pedir_codigo('Digite o código da reclamação que deseja atualizar: ')
    
    nova_descricao = input('Digite a nova descrição da reclamação: ')

    consulta = "update Ouvidoria set descricao = %s where codigo = %s and categoria = 'Reclamação';"
    dados = [nova_descricao, codigo]

    att = atualizarBancoDados(conexao, consulta, dados)


    if att > 0:
        print('Reclamação atualizada com sucesso!')

    else:
        print('Código informado é invalido')

def remover_reclamacao(conexao):
    codigo = pedir_codigo('Digite o código da reclamação que deseja remover: ')

    consulta = "delete from Ouvidoria where codigo = %s and categoria = 'Reclamação';"
    dados = [codigo]

    removidos = excluirBancoDados(conexao, consulta, dados)

    if removidos > 0:
        print('Reclamação removida com sucesso!')

    else:
        print('Código informado é invalido')

def registrar_denuncia(conexao):

    motivo = input('Digite o motivo da denúncia: ')
    descricao = input('Digite a sua denúncia: ')
    categoria = "Denuncia"
    consulta = 'insert into Ouvidoria (tipo, descricao, categoria) values (%s,%s,%s);'
    dados = [motivo, descricao, categoria]
    cod_denuncia = insertNoBancoDados(conexao, consulta, dados)

    print('Denúncia adicionada com sucesso, código da sua denúncia é:', cod_denuncia)

def listar_denuncias(conexao):

    consulta = "select * from Ouvidoria where categoria = 'Denuncia';"
    denuncias = listarBancoDados(conexao, consulta)

    if denuncias:

        print('Lista de Denúncias')
        exibir_itens(denuncias)
    
    else:
        print('Não existem denúncias a serem exibidas')

def pesquisar_denuncia(conexao):
    codigo = pedir_codigo('Digite o código da denúncia que deseja pesquisar: ')

    consulta = 'select * from Ouvidoria where codigo = %s and categoria = %s;'
    dados = [codigo, "Denuncia"]

    denuncias = listarBancoDados(conexao, consulta, dados)

    if denuncias:
        print('Denúncia Encontrada')
        exibir_itens(denuncias)
    else:
        print('Denúncia não encontrada')

def atualizar_denuncia(conexao):

    codigo = pedir_codigo('Digite o código da denúncia que deseja atualizar: ')
    
    nova_descricao = input('Digite a nova descrição da denúncia: ')

    consulta = "update Ouvidoria set descricao = %s where codigo = %s and categoria = 'Denuncia';"
    dados = [nova_descricao, codigo]

    att = atualizarBancoDados(conexao, consulta, dados)


    if att > 0:
        print('Denúncia atualizada com sucesso!')

    else:
        print('Código informado é invalido')

def remover_denuncia(conexao):
    codigo = pedir_codigo('Digite o código da denúncia que deseja remover: ')

    consulta = "delete from Ouvidoria where codigo = %s and categoria = 'Denuncia';"
    dados = [codigo]

    removidos = excluirBancoDados(conexao, consulta, dados)

    if removidos > 0:
        print('Denúncia removida com sucesso!')

    else:
        print('Código informado é invalido')

def registrar_sugestao(conexao):

    motivo = input('Digite o motivo da sugestão: ')
    descricao = input('Digite a sua sugestão: ')
    categoria = "Sugestão"
    consulta = 'insert into Ouvidoria (tipo, descricao, categoria) values (%s,%s,%s);'
    dados = [motivo, descricao, categoria]
    cod_sugestao = insertNoBancoDados(conexao, consulta, dados)

    print('Sugestão adicionada com sucesso, código da sua sugestão é:', cod_sugestao)

def listar_sugestoes(conexao):

    consulta = "select * from Ouvidoria where categoria = 'Sugestão';"
    sugestoes = listarBancoDados(conexao, consulta)

    if sugestoes:

        print('Lista de Sugestões')
        exibir_itens(sugestoes)
    
    else:
        print('Não existem sugestões a serem exibidas')

def pesquisar_sugestao(conexao):
    codigo = pedir_codigo('Digite o código da sugestão que deseja pesquisar: ')

    consulta = 'select * from Ouvidoria where codigo = %s and categoria = %s;'
    dados = [codigo, "Sugestão"]

    sugestoes = listarBancoDados(conexao, consulta, dados)

    if sugestoes:
        print('Sugestão Encontrada')
        exibir_itens(sugestoes)
    else:
        print('Sugestão não encontrada')

def atualizar_sugestao(conexao):

    codigo = pedir_codigo('Digite o código da sugestão que deseja atualizar: ')
    
    nova_descricao = input('Digite a nova descrição da sugestão: ')

    consulta = "update Ouvidoria set descricao = %s where codigo = %s and categoria = 'Sugestão';"
    dados = [nova_descricao, codigo]

    att = atualizarBancoDados(conexao, consulta, dados)


    if att > 0:
        print('Sugestão atualizada com sucesso!')

    else:
        print('Código informado é invalido')

def remover_sugestao(conexao):
    codigo = pedir_codigo('Digite o código da sugestão que deseja remover: ')

    consulta = "delete from Ouvidoria where codigo = %s and categoria = 'Sugestão';"
    dados = [codigo]

    removidos = excluirBancoDados(conexao, consulta, dados)

    if removidos > 0:
        print('Sugestão removida com sucesso!')

    else:
        print('Código informado é invalido')

def registrar_elogio(conexao):

    motivo = input('Digite o motivo do elogio: ')
    descricao = input('Digite o seu elogio: ')
    categoria = "Elogio"
    consulta = 'insert into Ouvidoria (tipo, descricao, categoria) values (%s,%s,%s);'
    dados = [motivo, descricao, categoria]
    cod_elogio = insertNoBancoDados(conexao, consulta, dados)

    print('Elogio adicionado com sucesso, código do seu elogio é:', cod_elogio)

def listar_elogios(conexao):

    consulta = "select * from Ouvidoria where categoria = 'Elogio';"
    elogios = listarBancoDados(conexao, consulta)

    if elogios:

        print('Lista de Elogios')
        exibir_itens(elogios)
    
    else:
        print('Não existem elogios a serem exibidos')

def pesquisar_elogio(conexao):
    codigo = pedir_codigo('Digite o código do elogio que deseja pesquisar: ')

    consulta = 'select * from Ouvidoria where codigo = %s and categoria = %s;'
    dados = [codigo, "Elogio"]

    elogios = listarBancoDados(conexao, consulta, dados)

    if elogios:
        print('Elogio Encontrado')
        exibir_itens(elogios)
    else:
        print('Elogio não encontrado')

def atualizar_elogio(conexao):

    codigo = pedir_codigo('Digite o código do elogio que deseja atualizar: ')
    
    nova_descricao = input('Digite a nova descrição do elogio: ')

    consulta = "update Ouvidoria set descricao = %s where codigo = %s and categoria = 'Elogio';"
    dados = [nova_descricao, codigo]

    att = atualizarBancoDados(conexao, consulta, dados)


    if att > 0:
        print('Elogio atualizado com sucesso!')

    else:
        print('Código informado é invalido')

def remover_elogio(conexao):
    codigo = pedir_codigo('Digite o código do elogio que deseja remover: ')

    consulta = "delete from Ouvidoria where codigo = %s and categoria = 'Elogio';"
    dados = [codigo]

    removidos = excluirBancoDados(conexao, consulta, dados)

    if removidos > 0:
        print('Elogio removido com sucesso!')

    else:
        print('Código informado é invalido')

def registrar_solicitacao(conexao):

    motivo = input('Digite o motivo da solicitação: ')
    descricao = input('Digite a sua solicitação: ')
    categoria = "Solicitação"
    consulta = 'insert into Ouvidoria (tipo, descricao, categoria) values (%s,%s,%s);'
    dados = [motivo, descricao, categoria]
    cod_solicitacao = insertNoBancoDados(conexao, consulta, dados)

    print('Solicitação adicionada com sucesso, código da sua solicitação é:', cod_solicitacao)

def listar_solicitacoes(conexao):

    consulta = "select * from Ouvidoria where categoria = 'Solicitação';"
    solicitacoes = listarBancoDados(conexao, consulta)

    if solicitacoes:

        print('Lista de Solicitações')
        exibir_itens(solicitacoes)
    
    else:
        print('Não existem solicitações a serem exibidas')  

def pesquisar_solicitacao(conexao):
    codigo = pedir_codigo('Digite o código da solicitação que deseja pesquisar: ')

    consulta = 'select * from Ouvidoria where codigo = %s and categoria = %s;'
    dados = [codigo, "Solicitação"]

    solicitacoes = listarBancoDados(conexao, consulta, dados)

    if solicitacoes:
        print('Solicitação Encontrada')
        exibir_itens(solicitacoes)
    else:
        print('Solicitação não encontrada')

def atualizar_solicitacao(conexao):

    codigo = pedir_codigo('Digite o código da solicitação que deseja atualizar: ')
    
    nova_descricao = input('Digite a nova descrição da solicitação: ')

    consulta = "update Ouvidoria set descricao = %s where codigo = %s and categoria = 'Solicitação';"
    dados = [nova_descricao, codigo]

    att = atualizarBancoDados(conexao, consulta, dados)


    if att > 0:
        print('Solicitação atualizada com sucesso!')

    else:
        print('Código informado é invalido')

def remover_solicitacao(conexao):
    codigo = pedir_codigo('Digite o código da solicitação que deseja remover: ')

    consulta = "delete from Ouvidoria where codigo = %s and categoria = 'Solicitação';"
    dados = [codigo]

    removidos = excluirBancoDados(conexao, consulta, dados)

    if removidos > 0:
        print('Solicitação removida com sucesso!')

    else:
        print('Código informado é invalido')


    