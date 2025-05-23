from rich import print as rprint

def inputint(msg):
    while True:
        numero = input(msg)
        if numero.isnumeric():
            return int(numero)
        rprint('[bold red]Digite um número![/]')


def inputfloat(msg):
    while True:
        numfloat = input(msg)
        try:
            numfloat = float(numfloat)
            return numfloat
        except ValueError:
            rprint('[bold red]Digite um número válido![/]')


def inputstr(msg):
    while True:
        texto = input(msg)
        if texto.strip():
            return texto
        rprint('[bold red]Digite um texto válido![/]')