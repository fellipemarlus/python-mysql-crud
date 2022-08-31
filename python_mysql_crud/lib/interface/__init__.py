import colorama
from colorama import Fore
from colorama import Style
colorama.init()


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro! digite um número inteiro.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


def linha(tam=40):
    print(f'{Fore.LIGHTCYAN_EX}-{Fore.RESET}' * tam)


def titulo(text):
    linha()
    print(f'{Style.BRIGHT}{text.center(40)}{Style.RESET_ALL}')
    linha()


def menu(lista):
    titulo("MENU DE OPÇÕES")
    c = 1
    for item in lista:
        print(f'{Fore.GREEN}{c}{Fore.RESET} - {item}')
        c += 1
    linha()
    opcao = leiaInt('Sua Opção: ')
    return opcao
