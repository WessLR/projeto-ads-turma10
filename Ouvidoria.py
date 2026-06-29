#GRUPO:
#ANDERSON ALMEIDA DA SILVA
#ISMAEL DA CONCEIÇÃO MOTA
#LEONARDO RUAN OLIVEIRA SANTOS
#RAQUEL BARROS LEAL



from operacoesbd import *

def pedir_codigo(mensagem):                 #Essa função vai pedir para o usuário digitar um código e vai verificar se o que ele digitou é um número inteiro. Se não for, ele vai mostrar uma mensagem de erro e pedir para o usuário digitar novamente. Ele vai continuar pedindo até que o usuário digite um número inteiro válido. Quando isso acontecer, a função vai retornar esse número inteiro.
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Erro: Digite apenas números! Tente novamente.')

def exibir_itens(itens):                    #Essa função vai receber uma lista de itens e vai exibir cada item da lista com o seu índice, título, descrição e código. Ela vai usar a função enumerate para percorrer a lista e obter o índice de cada item. O índice vai começar em 1. Para cada item, a função vai imprimir o índice, o título, a descrição e o código do item.
    for i, item in enumerate(itens, start=1):
        print(f'\n [{i}] Título: {item[1]}\n     Descrição: {item[2]}\n     Código: {item[0]}')


def registrar(conexao, categoria):          #Essa função vai receber a conexão com o banco de dados e a categoria da manifestação (Reclamação, Denúncia, Sugestão, Elogio ou Solicitação). Ela vai pedir para o usuário digitar o motivo e a descrição da manifestação. Depois, ela vai criar uma consulta SQL para inserir esses dados na tabela Ouvidoria do banco de dados. A consulta vai usar parâmetros (%s) para evitar SQL injection. Em seguida, a função vai chamar a função insertNoBancoDados para executar a consulta e inserir os dados no banco. Por fim, ela vai imprimir uma mensagem informando que a manifestação foi adicionada com sucesso e mostrar o código gerado pelo banco de dados.
    
    motivo = input(f'Digite o motivo da {categoria}: ')
    descricao = input(f'Digite a sua {categoria}: ')
    consulta = 'insert into Ouvidoria (tipo, descricao, categoria) values (%s,%s,%s);'
    dados = [motivo, descricao, categoria]
    cod = insertNoBancoDados(conexao, consulta, dados)

    print(f'{categoria} adicionada com sucesso! Código: {cod}')


def listar(conexao, categoria):             #Essa função vai receber a conexão com o banco de dados e a categoria da manifestação (Reclamação, Denúncia, Sugestão, Elogio ou Solicitação). Ela vai criar uma consulta SQL para selecionar todos os registros da tabela Ouvidoria que correspondam à categoria informada. A consulta vai usar um parâmetro (%s) para evitar SQL injection como o professor ensinou. Em seguida, a função vai chamar a função listarBancoDados para executar a consulta e obter os registros do banco de dados. Se houver registros, a função vai imprimir uma mensagem informando que a lista de manifestações foi encontrada e chamar a função exibir_itens para mostrar os registros. Caso contrário, ela vai imprimir uma mensagem informando que não existem manifestações a serem exibidas.

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
