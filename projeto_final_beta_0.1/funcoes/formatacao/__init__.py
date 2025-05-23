from decimal import Decimal
from rich import print as rprint
from rich.box import ROUNDED
from rich.table import Table

def mensagem(msg, cor:str=None):
    tamanho = len(msg) + 6
    if cor:
        rprint(f'{cor}=[/]' * tamanho)
    else:
        print('='* tamanho)
    print(f'{msg:^{tamanho}}')
    if cor:
        rprint(f'{cor}=[/]' * tamanho)
    else:
        print('='* tamanho)

def formatar_real(valor: Decimal | float) -> str:
    """Formata um valor Decimal ou float para a representação em Real (R$)."""
    return f"R$ {valor:.2f}".replace('.', ',')


def mostrar_tabela(tabela, titulo, *colunas, moeda=-1):
    """Mostra uma tabela utilizando rich, com formatação específica para valores."""
    table = Table(title=titulo, box=ROUNDED, header_style="bold blue")
    for coluna in colunas:
        table.add_column(f"[cyan]{coluna}[/cyan]", justify="right")
    for linha in tabela:
        linha_formatada = list(linha)
        if linha_formatada and isinstance(linha_formatada[moeda], Decimal):
            linha_formatada[moeda] = formatar_real(linha_formatada[moeda])
        table.add_row(*[str(dado) for dado in linha_formatada])
    rprint(table)

def mostrar_pedido(lista_pedido, titulo, *colunas):

    table = Table(title=titulo,  box=ROUNDED, header_style="bold blue")
    for coluna in colunas:
        table.add_column(f"[cyan]{coluna}[/cyan]", justify="right")
    numero = 0
    valor_total = 0
    for pedido in lista_pedido:
        numero += 1
        valor = pedido['quantidade'] * pedido['valor']
        valor_total += valor 
        table.add_row(str(numero), 
                      pedido['nome'], 
                      str(pedido['quantidade']), 
                      formatar_real(pedido['valor']), 
                      formatar_real(valor),
                      '')
    table.add_row('', '', '',  '', '', formatar_real(valor_total))
    
    rprint(table)


def valortotal(lista_pedido:list, formatado=False):
    
    numero = 0
    valor_total = 0
    for pedido in lista_pedido:
        numero += 1
        valor = pedido['quantidade'] * pedido['valor']
        valor_total += valor
    
    if formatado:
        return formatar_real(valor_total)
    else:
        return round(valor_total, 2) 

def mostrar_dados(lista:list, titulo, *colunas):

    table = Table(title=titulo, box=ROUNDED, header_style="bold blue")
    for coluna in colunas:
        table.add_column(f"[cyan]{coluna}[/cyan]", justify="right")
    table.add_row(*lista)
    rprint(table)