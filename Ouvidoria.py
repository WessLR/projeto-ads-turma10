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


def registrar(conexao, categoria):
    motivo = input(f'Digite o motivo da {categoria}: ')
    descricao = input(f'Digite a sua {categoria}: ')
    consulta = 'insert into Ouvidoria (tipo, descricao, categoria) values (%s,%s,%s);'
    dados = [motivo, descricao, categoria]
    cod = insertNoBancoDados(conexao, consulta, dados)
    print(f'{categoria} adicionada com sucesso! Código: {cod}')


def listar(conexao, categoria):

    consulta = "select * from Ouvidoria where categoria = %s;"
    reclamacoes = listarBancoDados(conexao, consulta, [categoria])

    if reclamacoes:

        print(f'Lista de {categoria}')
        exibir_itens(reclamacoes)
    
    else:
        print(f'Não existem {categoria} a serem exibidas')

def pesquisar(conexao, categoria):
    codigo = pedir_codigo(f'Digite o código da {categoria} que deseja pesquisar: ')

    consulta = 'select * from Ouvidoria where codigo = %s and categoria = %s;'
    dados = [codigo, categoria]

    itens = listarBancoDados(conexao, consulta, dados)

    if itens:
        print(f'{categoria} Encontrada')
        exibir_itens(itens)
    else:
        print(f'{categoria} não encontrada')

def atualizar(conexao, categoria):

    codigo = pedir_codigo(f'Digite o código da {categoria} que deseja atualizar: ')
    
    nova_descricao = input(f'Digite a nova descrição da {categoria}: ')

    consulta = f"update Ouvidoria set descricao = %s where codigo = %s and categoria = %s;"
    dados = [nova_descricao, codigo, categoria]

    att = atualizarBancoDados(conexao, consulta, dados)


    if att > 0:
        print(f'{categoria} atualizada com sucesso!')

    else:
        print('Código informado é invalido')

def remover(conexao, categoria):
    codigo = pedir_codigo(f'Digite o código da {categoria} que deseja remover: ')

    consulta = f"delete from Ouvidoria where codigo = %s and categoria = %s;"
    dados = [codigo, categoria]

    removidos = excluirBancoDados(conexao, consulta, dados)

    if removidos > 0:
        print(f'{categoria} removida com sucesso!')

    else:
        print('Código informado é invalido')

def relatorio(conexao):

    total = listarBancoDados(
        conexao,
        "select * from Ouvidoria;"
    )

    reclamacoes = listarBancoDados(
        conexao,
        "select * from Ouvidoria where categoria = 'Reclamação';"
    )

    sugestoes = listarBancoDados(
        conexao,
        "select * from Ouvidoria where categoria = 'Sugestão';"
    )

    elogios = listarBancoDados(
        conexao,
        "select * from Ouvidoria where categoria = 'Elogio';"
    )

    denuncias = listarBancoDados(
        conexao,
        "select * from Ouvidoria where categoria = 'Denúncia';"
    )

    print("\n===== RELATÓRIOS =====")
    print("Total de manifestações:", len(total))
    print("Reclamações:", len(reclamacoes))
    print("Sugestões:", len(sugestoes))
    print("Elogios:", len(elogios))
    print("Denúncias:", len(denuncias))

encerrarConexao(conexao)