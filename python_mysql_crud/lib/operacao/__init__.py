import mysql.connector
from mysql.connector import Error
from time import sleep
import colorama
from colorama import Fore
from colorama import Style
colorama.init()


def conectar():
    print('Estabelecendo conexão com o Banco de Dados... '), sleep(3)
    global conexao
    try:
        conexao = mysql.connector.connect(host='localhost', database='sistema_teste', user='root', password='')
    except Error as erro:
        print(f'{Fore.LIGHTRED_EX}Falha ao se conectar com o Banco de Dados:{Fore.RESET} {erro}')
    finally:
        print(f'{Fore.LIGHTGREEN_EX}Banco de dados conectado com sucesso{Fore.RESET}'), sleep(1)


def close():
    return conexao.close()


def create():
    nome_produto = str(input('Digite o nome do produto: ')).strip()
    preco_produto = str(input('Digite o preço do produto: R$')).strip()
    quantidade_produto = str(input('Digite a quantidade do produto no estoque: ')).strip()
    dados = f'\'{nome_produto}\', \'{preco_produto}\', \'{quantidade_produto}\''
    print(f'\n{Fore.LIGHTBLUE_EX}Inserindo os dados no Banco de Dados...{Fore.RESET}'), sleep(2)

    # Declaração SQL a ser executada
    inserir_dados = f"""INSERT INTO produtos (NomeProuto, Preco, Quantidade)
                                    VALUES
                                    ({dados});"""
    # Criar cursor e executar a SQL no BD
    try:
        cursor = conexao.cursor()
        cursor.execute(inserir_dados)
        # Sempre que acontecer uma alteração no BD, é necessário commitar para validar a transação
        conexao.commit()
        cursor.close()
    except Error as e:
        print(f'{Fore.LIGHTRED_EX}Falha ao inserir dados no Banco de Dados:{Fore.RESET} {e}')
    finally:
        print(f'{Fore.LIGHTGREEN_EX}Registro inserido com sucesso!{Fore.RESET}'), sleep(2)


def read():
    # Declaração SQL a ser executada
    consulta_dados = "SELECT * FROM produtos;"
    try:
        # Criar cursor e executar a SQL no BD
        cursor = conexao.cursor()
        cursor.execute(consulta_dados)
        linhas = cursor.fetchall()  # fetchall retorna todas as linhas em formato de lista()
        print(f'{Fore.LIGHTBLUE_EX}Realizando consulta no banco de dados...{Fore.RESET}'), sleep(2)
        print(f'Foram retornados {cursor.rowcount} registros.\n'), sleep(1)

        print("{:<3} {:^20} {:^14} {:^12}".format('ID', 'Produto', 'Preço', 'Quantidade'))
        print(f'-' * 3, '-' * 20, '-' * 14, '-' * 12)

        for linha in linhas:
            id_prod, produto, preco, quant = linha
            print("{:<3} {:<20} R${:<14} {:^12}".format(id_prod, produto, preco, quant))
        print('\nCarregando menu de opções...'), sleep(4)
    except Error as erro:
        print(f'{Fore.LIGHTRED_EX}Erro ao consultar os dados:{Fore.RESET} {erro}')


def update():
    linha = int(input('Digite o ID do produto que você quer atualizar: '))
    print('\nCOLUNAS DA TABELA : NomeProduto, Preco, Quantidade')
    print('O que você quer atualizar desse produto ?')
    coluna = input('Digite o nome da coluna que será atualizada: ').strip()
    valor = input('\nDigite o novo valor: ')
    print(f'\n{Fore.LIGHTBLUE_EX}Atualizando os dados no Banco de Dados...{Fore.RESET}'), sleep(2)

    # Declaração SQL a ser executada
    atualizar_dados = f"UPDATE produtos SET {coluna} = '{valor}' WHERE produtos.idProduto = {linha};"
    # Criar cursor e executar a SQL no BD
    try:
        cursor = conexao.cursor()
        cursor.execute(atualizar_dados)
        # Sempre que acontecer uma alteração no BD, é necessário commitar para validar a transação
        conexao.commit()
        cursor.close()
    except Error as e:
        print(f'{Fore.LIGHTRED_EX}Falha ao atualizar dados no Banco de Dados: {Fore.RESET}{e}')
    finally:
        print(f'{Fore.LIGHTGREEN_EX}Registro atualizado com sucesso!{Fore.RESET}'), sleep(2)


def delete():
    conf = ' '
    while conf not in 'SN':
        linha = int(input('Digite o ID do produto que você quer deletar: '))
        print(f'{Fore.LIGHTYELLOW_EX}*** Decisão irreversível ***{Fore.RESET}')
        conf = str(input(f'{Fore.LIGHTYELLOW_EX}Tem certeza que quer deletar esse produto? [S/N]:{Fore.RESET} ')).strip().upper()[0]
        if conf == 'S':
            print(f'\n{Fore.LIGHTRED_EX}Deletando o produto do Banco de Dados...{Fore.RESET}'), sleep(2)
            # Declaração SQL a ser executada
            deletar_dados = f"DELETE FROM produtos WHERE produtos.idProduto = {linha};"
            # Criar cursor e executar a SQL no BD
            try:
                cursor = conexao.cursor()
                cursor.execute(deletar_dados)
                # Sempre que acontecer uma alteração no BD, é necessário commitar para validar a transação
                conexao.commit()
                cursor.close()
            except Error as e:
                print(f'{Fore.LIGHTYELLOW_EX}Falha ao deletar o produto no Banco de Dados: {Fore.RESET}{e}')
            finally:
                print(f'{Fore.LIGHTRED_EX}Produto deletado com sucesso!{Fore.RESET}'), sleep(2)

        elif conf == 'N':
            print('Você desistiu da operação')
            break
        else:
            print('Opção inválida')
