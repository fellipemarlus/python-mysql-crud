from lib import operacao, interface
interface.titulo('Cadastro de produtos no Banco de Dados')

operacao.conectar()

while True:
    opcao = interface.menu(["Cadastrar um novo produto", "Consultar todos os dados da tabela",
                            "Atualizar dados na tabela", "Deletar dados na tabela", "Sair"])
    if opcao == 1:
        operacao.create()
    elif opcao == 2:
        operacao.read()
    elif opcao == 3:
        operacao.update()
    elif opcao == 4:
        operacao.delete()
    elif opcao not in (1, 2, 3, 4, 5):
        print('Opção inválida, digite uma opção válida')
    else:
        operacao.close()
        print('Conexão com o banco de dados encerrada.')
        break
